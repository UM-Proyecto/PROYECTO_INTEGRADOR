"""Genera o comprueba fuentes/MANIFIESTO.csv (sha256 y tamaño de cada copia en fuentes/).

Uso:
  python3 verificacion/manifiesto.py --generar   # sólo al incorporar una fuente nueva
  python3 verificacion/manifiesto.py             # comprueba que ninguna copia cambió
Sale con código 1 si una copia no coincide, falta o sobra.
"""
import csv, hashlib, pathlib, sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
FUENTES = RAIZ / "fuentes"
MANIFIESTO = FUENTES / "MANIFIESTO.csv"
REPO = "UM-Proyecto/MINERIA_DATOS"
COMMIT = "c27757a"
ORIGEN = {  # copia -> ruta original en el repositorio del equipo
    "F01_pregunta_enfocada/PREGUNTA ENFOCADA Y OBJETIVO.docx": "docs/pregunta-enfocada/PREGUNTA ENFOCADA Y OBJETIVO.docx",
    "F02_registro_fuentes_HU02/registro_actualizaciones.csv": "data/processed/hu-02/registro_actualizaciones.csv",
    "F02_registro_fuentes_HU02/conjuntos.csv": "data/raw/hu-02/conjuntos.csv",
    "F02_registro_fuentes_HU02/historial_cargas.csv": "data/processed/hu-02/historial_cargas.csv",
    "F02_registro_fuentes_HU02/LEEME.md": "docs/hu-02/LEEME.md",
    "F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md": "docs/hu-33/CRITERIOS_APROBADOS.md",
    "F03_criterios_exito_HU33/BORRADOR_criterios_exito.md": "docs/hu-33/BORRADOR_criterios_exito.md",
    "F04_pronosticos_HU07/comparacion_pronosticos.csv": "data/processed/hu-07/comparacion_pronosticos.csv",
    "F04_pronosticos_HU07/README.md": "docs/hu-07/README.md",
    "F05_costos_importacion_HU31/hu31_costos_importacion.csv": "data/processed/hu-30-31/hu31_costos_importacion.csv",
    "F05_costos_importacion_HU31/flete_referencias_puntuales.csv": "data/raw/hu-30-31/insumos_publicos/flete_referencias_puntuales.csv",
    "F05_costos_importacion_HU31/SHA256SUMS_insumos_publicos.txt": "data/raw/hu-30-31/insumos_publicos/SHA256SUMS.txt",
    "F05_costos_importacion_HU31/LEEME_hu30-31.md": "docs/hu-30-31/LEEME.md",
    "F06_portada_repositorio/README.md": "README.md",
    "F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md": "docs/hu-34/HU34_Descripcion_Datos_MULTIPARTE.md",
    "F07_datos_simulados_HU34/ventas_simuladas.csv": "data/raw/hu-34/ventas_simuladas.csv",
    "F07_datos_simulados_HU34/Guia_Limpieza.md": "docs/hu-34/Guia_Limpieza.md",
}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def copias():
    return sorted(str(p.relative_to(FUENTES)) for p in FUENTES.rglob("*")
                  if p.is_file() and p.name not in ("MANIFIESTO.csv", "MANIFIESTO.md"))


def generar():
    filas = []
    for rel in copias():
        p = FUENTES / rel
        filas.append({"copia": rel, "origen_repo": REPO, "commit": COMMIT,
                      "ruta_original": ORIGEN.get(rel, "?"), "bytes": p.stat().st_size, "sha256": sha(p)})
    with MANIFIESTO.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(filas[0]))
        w.writeheader(); w.writerows(filas)
    print(f"MANIFIESTO.csv: {len(filas)} copias")


def comprobar():
    fallas = 0
    filas = list(csv.DictReader(MANIFIESTO.open(encoding="utf-8")))
    declaradas = {f["copia"] for f in filas}
    for f in filas:
        p = FUENTES / f["copia"]
        if not p.exists():
            print("FALTA", f["copia"]); fallas += 1
        elif sha(p) != f["sha256"]:
            print("CAMBIÓ", f["copia"]); fallas += 1
        else:
            print("OK", f["copia"])
    for rel in set(copias()) - declaradas:
        print("SOBRA (no está en el manifiesto)", rel); fallas += 1
    print(f"{len(filas) - fallas} de {len(filas)} copias intactas")
    sys.exit(1 if fallas else 0)


if __name__ == "__main__":
    generar() if "--generar" in sys.argv else comprobar()
