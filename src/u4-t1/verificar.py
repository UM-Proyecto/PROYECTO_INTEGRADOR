"""Recalcula desde fuentes/ las cifras que la consulta de la wiki afirma, y las compara con lo esperado.

Uso:  python3 src/u4-t1/verificar.py [--csv data/processed/u4-t1/verificaciones.csv]
Sólo biblioteca estándar. Cada verificación imprime el valor recalculado, el valor afirmado y OK o DIFIERE.
Sale con código 1 si alguna difiere.
"""
import csv, datetime as dt, os, pathlib, re, sys, zipfile
from collections import Counter

RAIZ = pathlib.Path(os.environ.get("PI_RAIZ") or pathlib.Path(__file__).resolve().parents[2])
F = RAIZ / "fuentes"


def leer(rel):
    with open(F / rel, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def texto_docx(rel):
    x = zipfile.ZipFile(F / rel).read("word/document.xml").decode("utf-8")
    parrafos = re.findall(r"<w:p[ >].*?</w:p>", x, flags=re.S)
    return "\n".join("".join(re.findall(r"<w:t[^>]*>([^<]*)</w:t>", p)) for p in parrafos)


def dias(a, b):
    return (dt.date.fromisoformat(b) - dt.date.fromisoformat(a)).days


VERIF = []


def verif(codigo, afirmacion, fuente):
    def deco(fn):
        VERIF.append((codigo, afirmacion, fuente, fn))
        return fn
    return deco


@verif("V1", "KPI-2: 6 de 15 componentes del costo de importación están DOCUMENTADOS (40 %); 5 son ESTIMACION y 4 PENDIENTE",
       "F05 hu31_costos_importacion.csv, columna tipo_dato")
def v1():
    c = Counter(r["tipo_dato"] for r in leer("F05_costos_importacion_HU31/hu31_costos_importacion.csv"))
    total = sum(c.values())
    calc = (c["DOCUMENTADO"], total, round(100 * c["DOCUMENTADO"] / total, 1), c["ESTIMACION"], c["PENDIENTE"])
    return calc, (6, 15, 40.0, 5, 4)


@verif("V2", "KPI-1: ningún método es elegible; las 30 filas (10 repuestos por 3 métodos) dicen SIN_SELECCION_FIABLE y la evaluación cubre del 10 al 14-sep-2026",
       "F04 comparacion_pronosticos.csv, columnas codigo_unico, metodo, seleccion, desde_evaluacion, hasta_evaluacion")
def v2():
    r = leer("F04_pronosticos_HU07/comparacion_pronosticos.csv")
    calc = (len(r), len({x["codigo_unico"] for x in r}), len({x["metodo"] for x in r}),
            sorted({x["seleccion"] for x in r}), min(x["desde_evaluacion"] for x in r), max(x["hasta_evaluacion"] for x in r))
    return calc, (30, 10, 3, ["SIN_SELECCION_FIABLE"], "2026-09-10", "2026-09-14")


@verif("V3", "KPI-3: los movimientos de inventario llegan al 14-sep-2026; son 42 días al 26-oct-2026 (línea base) y 50 días al 3-nov-2026",
       "F02 registro_actualizaciones.csv, fila movimientos_inventario, columna fecha_corte_datos; fechas de F03")
def v3():
    fila = {r["conjunto"]: r for r in leer("F02_registro_fuentes_HU02/registro_actualizaciones.csv")}["movimientos_inventario"]
    corte = fila["fecha_corte_datos"]
    return (corte, dias(corte, "2026-10-26"), dias(corte, "2026-11-03")), ("2026-09-14", 42, 50)


@verif("V4", "El registro de la HU-02 tiene 17 conjuntos: 13 FICTICIO, 3 PUBLICO y 1 MIXTO, todos con carga OK",
       "F02 registro_actualizaciones.csv, columnas tipo_dato y estado_ultima_carga")
def v4():
    r = leer("F02_registro_fuentes_HU02/registro_actualizaciones.csv")
    c = Counter(x["tipo_dato"] for x in r)
    return (len(r), c["FICTICIO"], c["PUBLICO"], c["MIXTO"], sorted({x["estado_ultima_carga"] for x in r})), (17, 13, 3, 1, ["OK"])


@verif("V5", "La pregunta enfocada de F01 habla de decisiones de compra de MULTIPARTES en el segundo semestre de 2026",
       "F01 PREGUNTA ENFOCADA Y OBJETIVO.docx")
def v5():
    t = texto_docx("F01_pregunta_enfocada/PREGUNTA ENFOCADA Y OBJETIVO.docx")
    frase = "apoyar las decisiones de compra de la empresa MULTIPARTES"
    return (frase in t, "segundo semestre del 2026" in t), (True, True)


def main():
    filas, fallas = [], 0
    for codigo, afirm, fuente, fn in VERIF:
        calc, esperado = fn()
        ok = calc == esperado
        fallas += not ok
        print(f"{codigo} {'OK' if ok else 'DIFIERE'}: {afirm}\n    recalculado={calc}\n    afirmado={esperado}\n    fuente: {fuente}")
        filas.append({"codigo": codigo, "afirmacion": afirm, "fuente": fuente,
                      "recalculado": repr(calc), "afirmado": repr(esperado), "resultado": "OK" if ok else "DIFIERE"})
    if "--csv" in sys.argv:
        salida = RAIZ / sys.argv[sys.argv.index("--csv") + 1]
        salida.parent.mkdir(parents=True, exist_ok=True)
        with salida.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(filas[0])); w.writeheader(); w.writerows(filas)
    print(f"{len(VERIF) - fallas} de {len(VERIF)} verificaciones coinciden")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    main()
