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


# Verificaciones de la consulta Q-01 (revisión 02)

@verif("Q1", "Q-01, KPI-1: la mejora frente a «último periodo» es 0 % para el promedio móvil y -128,6 % para el mismo día de la semana (MAE medio de 10 repuestos)",
       "F04 comparacion_pronosticos.csv, columnas metodo y mae")
def q1():
    r = leer("F04_pronosticos_HU07/comparacion_pronosticos.csv")
    media = {m: sum(float(x["mae"]) for x in r if x["metodo"] == m) / 10 for m in ("ultimo_periodo", "promedio_movil_3", "mismo_dia_semana")}
    b = media["ultimo_periodo"]
    return (round((b - media["promedio_movil_3"]) / b * 100, 1), round((b - media["mismo_dia_semana"]) / b * 100, 1)), (0.0, -128.6)


@verif("Q1b", "Q-01, corrección: en los 3 repuestos con ventas en la evaluación los tres métodos empatan (MAE medio 0,467); "
       "todo el -128,6 % sale de 2 repuestos sin ventas en los que «mismo día de la semana» pronosticó ventas",
       "F04 comparacion_pronosticos.csv, columnas codigo_unico, metodo, mae y dias_con_ventas_evaluacion")
def q1b():
    r = leer("F04_pronosticos_HU07/comparacion_pronosticos.csv")
    con = {x["codigo_unico"] for x in r if x["metodo"] == "ultimo_periodo" and x["dias_con_ventas_evaluacion"] != "0"}
    medias = sorted({round(sum(float(x["mae"]) for x in r if x["metodo"] == m and x["codigo_unico"] in con) / len(con), 3)
                     for m in ("ultimo_periodo", "promedio_movil_3", "mismo_dia_semana")})
    sin_ventas_con_error = sorted(x["codigo_unico"] for x in r
                                  if x["codigo_unico"] not in con and float(x["mae"]) > 0)
    return (len(con), medias, sin_ventas_con_error), (3, [0.467], ["REP-0001", "REP-0003"])


@verif("Q2", "Q-01, KPI-3: para cumplir la meta al 3-nov-2026 el corte debe llegar al 2026-10-04; el actual (2026-09-14) está 20 días antes",
       "F02 registro_actualizaciones.csv, fila movimientos_inventario; meta de 30 días de F03")
def q2():
    corte = {r["conjunto"]: r for r in leer("F02_registro_fuentes_HU02/registro_actualizaciones.csv")}["movimientos_inventario"]["fecha_corte_datos"]
    limite = (dt.date(2026, 11, 3) - dt.timedelta(days=30)).isoformat()
    return (limite, dias(corte, limite)), ("2026-10-04", 20)


@verif("Q3", "Q-01, KPI-2: con los 4 pendientes documentados se llega a 66,7 %; contando además las 5 estimaciones del INE, a 73,3 %; la meta pide 12 de 15",
       "F05 hu31_costos_importacion.csv, columna tipo_dato; meta de F03")
def q3():
    c = Counter(r["tipo_dato"] for r in leer("F05_costos_importacion_HU31/hu31_costos_importacion.csv"))
    t = sum(c.values())
    return (round(100 * (c["DOCUMENTADO"] + c["PENDIENTE"]) / t, 1), round(100 * (c["DOCUMENTADO"] + c["ESTIMACION"]) / t, 1),
            int(0.8 * t)), (66.7, 73.3, 12)


# Verificaciones de la segunda ingesta (revisión 04)

@verif("I2-1", "F07: ventas_simuladas tiene 19.860 filas, 30 repuestos y 662 días seguidos del 2025-01-01 al 2026-10-24, sin claves fecha + sku repetidas",
       "F07 ventas_simuladas.csv, columnas fecha y sku")
def i2_1():
    r = leer("F07_datos_simulados_HU34/ventas_simuladas.csv")
    f = sorted({x["fecha"] for x in r})
    seguidos = dias(f[0], f[-1]) + 1
    return (len(r), len({x["sku"] for x in r}), len(f), seguidos, f[0], f[-1], len(r) - len({(x["fecha"], x["sku"]) for x in r})), \
           (19860, 30, 662, 662, "2025-01-01", "2026-10-24", 0)


@verif("I2-2", "F07: reservando los 3 últimos meses (92 días desde el 2026-07-25), en el año de entrenamiento anterior cada repuesto tiene al menos 246 días con ventas",
       "F07 ventas_simuladas.csv, columnas fecha, sku y unidades_vendidas")
def i2_2():
    r = leer("F07_datos_simulados_HU34/ventas_simuladas.csv")
    ini_reserva, fin = dt.date(2026, 7, 25), dt.date(2026, 10, 24)
    ini_ent = ini_reserva - dt.timedelta(days=365)
    c = Counter(x["sku"] for x in r if ini_ent <= dt.date.fromisoformat(x["fecha"]) < ini_reserva and int(x["unidades_vendidas"]) > 0)
    return ((fin - ini_reserva).days + 1, len(c), min(c.values())), (92, 30, 246)


@verif("I2-3", "KPI-3 tras la segunda ingesta: con las ventas de F07 (corte 2026-10-24) son 10 días al 3-nov-2026 y cumplirían la meta hasta el 2026-11-23; con los movimientos de F03 siguen siendo 50",
       "F07 ventas_simuladas.csv, columna fecha; F02 fila movimientos_inventario")
def i2_3():
    corte_v = max(x["fecha"] for x in leer("F07_datos_simulados_HU34/ventas_simuladas.csv"))
    corte_m = {r["conjunto"]: r for r in leer("F02_registro_fuentes_HU02/registro_actualizaciones.csv")}["movimientos_inventario"]["fecha_corte_datos"]
    return (dias(corte_v, "2026-11-03"), (dt.date.fromisoformat(corte_v) + dt.timedelta(days=30)).isoformat(), dias(corte_m, "2026-11-03")), \
           (10, "2026-11-23", 50)


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
