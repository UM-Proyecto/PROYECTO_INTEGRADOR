"""Revisión de salud determinista de wiki/ (complementa la revisión que hace el agente).

Uso:  python3 src/u4-t1/salud.py [--json salida.json]
Controles:
  enlaces_rotos       enlace relativo de Markdown a un archivo que no existe
  huerfanas           página de wiki/ que no está enlazada desde index.md
  sin_metadatos       página sin bloque YAML o sin alguno de los campos obligatorios
  kpi_incompletos     página de indicador sin alguno de los campos de definición
  sin_etiqueta        párrafo o ítem con una cifra y sin ninguna etiqueta de afirmación
  sin_cita            párrafo o ítem con etiqueta [OBSERVADO] o [CALCULADO] sin enlace a fuentes/
  frase_prohibida     «no entregó» / «no proporcionó» fuera de una cita textual marcada
  titulos_duplicados  dos páginas con el mismo título de nivel 1
Sale con código 1 si hay algún hallazgo.
"""
import json, os, pathlib, re, sys
from urllib.parse import unquote

RAIZ = pathlib.Path(os.environ.get("PI_RAIZ") or pathlib.Path(__file__).resolve().parents[2])
WIKI = RAIZ / "wiki"
CAMPOS_META = ("tipo", "fuentes", "fecha_datos", "estado", "actualizado")
CAMPOS_KPI = ("fórmula", "unidad", "granularidad", "período", "filtros", "meta", "línea base")
ETIQUETAS = ("[OBSERVADO]", "[CALCULADO]", "[INFERENCIA]", "[SUPUESTO]", "[ESPERADO]")
ENLACE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
CIFRA = re.compile(r"(?<![\w-])\d+(?:[.,]\d+)?\s?(?:%|días|de \d+)")


def paginas():
    return sorted(WIKI.rglob("*.md"))


def bloques(texto):
    """Párrafos e ítems de lista fuera de bloques de código y del YAML inicial."""
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    for b in re.split(r"\n\s*\n|\n(?=\s*[-*] |\s*\d+\. |\|)", texto):
        b = b.strip()
        if b and not b.startswith("#"):
            yield b


def main():
    h = {k: [] for k in ("enlaces_rotos", "huerfanas", "sin_metadatos", "kpi_incompletos",
                         "sin_etiqueta", "sin_cita", "frase_prohibida", "titulos_duplicados")}
    pags = paginas()
    if not pags:
        print("wiki/ vacía"); sys.exit(1)
    indice = WIKI / "index.md"
    enlazadas_desde_indice = set()
    titulos = {}
    for p in pags:
        rel = p.relative_to(RAIZ).as_posix()
        t = p.read_text(encoding="utf-8")
        for destino in ENLACE.findall(t):
            if re.match(r"^[a-z]+://|^mailto:|^#", destino):
                continue
            ruta = unquote(destino.split("#")[0])
            if not ruta:
                continue
            obj = (p.parent / ruta).resolve()
            if not obj.exists():
                h["enlaces_rotos"].append(f"{rel} -> {destino}")
            elif p == indice:
                enlazadas_desde_indice.add(obj)
        m = re.match(r"\A---\n(.*?)\n---\n", t, flags=re.S)
        if p.name not in ("index.md", "log.md"):
            if not m:
                h["sin_metadatos"].append(f"{rel}: sin bloque YAML")
            else:
                faltan = [c for c in CAMPOS_META if not re.search(rf"^{c}\s*:", m.group(1), flags=re.M)]
                if faltan:
                    h["sin_metadatos"].append(f"{rel}: faltan {', '.join(faltan)}")
        if "indicadores" in p.parts:
            baja = t.lower()
            faltan = [c for c in CAMPOS_KPI if c not in baja]
            if faltan:
                h["kpi_incompletos"].append(f"{rel}: faltan {', '.join(faltan)}")
        if p.name not in ("log.md",):
            for b in bloques(t):
                tiene_etiqueta = any(e in b for e in ETIQUETAS)
                if CIFRA.search(b) and not tiene_etiqueta and not b.startswith("|") and p.name != "index.md":
                    h["sin_etiqueta"].append(f"{rel}: {b[:90]!r}")
                if ("[OBSERVADO]" in b or "[CALCULADO]" in b) and "fuentes/" not in b:
                    h["sin_cita"].append(f"{rel}: {b[:90]!r}")
                for frase in ("no entregó", "no proporcionó", "no se proporcionaron", "no entregaron"):
                    if frase in b.lower() and "«" not in b:
                        h["frase_prohibida"].append(f"{rel}: {frase}")
        m1 = re.search(r"^# (.+)$", t, flags=re.M)
        if m1:
            titulos.setdefault(m1.group(1).strip().lower(), []).append(rel)
    for p in pags:
        if p != indice and p.resolve() not in enlazadas_desde_indice:
            h["huerfanas"].append(p.relative_to(RAIZ).as_posix())
    for t, rs in titulos.items():
        if len(rs) > 1:
            h["titulos_duplicados"].append(f"{t}: {', '.join(rs)}")
    total = 0
    print(f"páginas revisadas: {len(pags)}")
    for k, v in h.items():
        total += len(v)
        print(f"{k}: {len(v)}")
        for x in v:
            print("   ", x)
    if "--json" in sys.argv:
        pathlib.Path(sys.argv[sys.argv.index("--json") + 1]).write_text(
            json.dumps({"paginas": len(pags), "hallazgos": h}, ensure_ascii=False, indent=1), encoding="utf-8")
    sys.exit(1 if total else 0)


if __name__ == "__main__":
    main()
