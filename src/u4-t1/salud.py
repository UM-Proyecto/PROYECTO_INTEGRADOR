"""Revisión de salud determinista de wiki/ (complementa la revisión que hace el agente).

Uso:  python3 src/u4-t1/salud.py [--json salida.json]
Entiende los dos tipos de enlace que usa la wiki: [[wikilink]] de Obsidian entre páginas y enlace
Markdown relativo hacia fuentes/. Controles:
  enlaces_rotos       enlace Markdown a un archivo que no existe
  wikilinks_rotos     [[nombre]] o [[nombre#Encabezado]] que no resuelve a una página o a un encabezado
  huerfanas           página de wiki/ sin ningún enlace entrante desde otra página
  fuera_del_indice    página que index.md (el MOC) no enlaza
  sin_metadatos       página sin bloque YAML o sin alguno de los campos obligatorios
  kpi_incompletos     página de indicador sin alguno de los campos de definición
  sin_etiqueta        párrafo o ítem con una cifra y sin ninguna etiqueta de afirmación
  sin_cita            [OBSERVADO] o [CALCULADO] sin enlace a una fuente ni a otra página; una fila de
                      tabla vale como citada si el párrafo que presenta la tabla cita una fuente
  frase_prohibida     «no entregó» / «no proporcionó» fuera de una cita textual entre comillas
  titulos_duplicados  dos páginas con el mismo título de nivel 1
  nombres_duplicados  dos páginas con el mismo nombre de archivo (rompe la resolución de [[nombre]])
Sale con código 1 si hay algún hallazgo.
"""
import json, os, pathlib, re, sys
from urllib.parse import unquote

RAIZ = pathlib.Path(os.environ.get("PI_RAIZ") or pathlib.Path(__file__).resolve().parents[2])
WIKI = RAIZ / "wiki"
CAMPOS_META = ("tipo", "fuentes", "fecha", "estado", "revision", "actualizado", "tags")
CAMPOS_KPI = ("fórmula", "unidad", "granularidad", "período", "filtros", "meta", "línea base")
ETIQUETAS = ("[OBSERVADO]", "[CALCULADO]", "[INFERENCIA]", "[SUPUESTO]", "[ESPERADO]")
ENLACE_MD = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|[^\]]*)?\]\]")
CIFRA = re.compile(r"(?<![\w-])\d+(?:[.,]\d+)?\s?(?:%|días|de \d+)")


def bloques(texto):
    """Párrafos, ítems y filas de tabla fuera de bloques de código y del YAML inicial."""
    texto = re.sub(r"\A---\n.*?\n---\n", "", texto, flags=re.S)
    texto = re.sub(r"```.*?```", "", texto, flags=re.S)
    texto = re.sub(r"(?m)^(?: {4}|\t).*$", "", texto)  # bloques de código con sangría
    for b in re.split(r"\n\s*\n|\n(?=\s*[-*] |\s*\d+\. |\|)", texto):
        b = b.strip()
        if b and not b.startswith("#"):
            yield b


def encabezados(p):
    return {h.strip().lower() for h in re.findall(r"^#{1,6} (.+)$", p.read_text(encoding="utf-8"), flags=re.M)}


def main():
    h = {k: [] for k in ("enlaces_rotos", "wikilinks_rotos", "huerfanas", "fuera_del_indice", "sin_metadatos",
                         "kpi_incompletos", "sin_etiqueta", "sin_cita", "frase_prohibida", "titulos_duplicados",
                         "nombres_duplicados")}
    pags = sorted(WIKI.rglob("*.md"))
    if not pags:
        print("wiki/ vacía"); sys.exit(1)
    # destinos de [[nombre]]: las páginas de la wiki y los .md de la raíz (AGENTS.md, README.md)
    por_nombre = {}
    for p in pags + sorted(RAIZ.glob("*.md")):
        por_nombre.setdefault(p.stem.lower(), []).append(p)
    for n, ps in por_nombre.items():
        if len(ps) > 1:
            h["nombres_duplicados"].append(f"{n}: {', '.join(x.relative_to(RAIZ).as_posix() for x in ps)}")
    indice = WIKI / "index.md"
    entrantes = {p: set() for p in pags}
    titulos = {}
    for p in pags:
        rel = p.relative_to(RAIZ).as_posix()
        t = p.read_text(encoding="utf-8")
        for destino in ENLACE_MD.findall(t):
            if re.match(r"^[a-z]+://|^mailto:|^#", destino):
                continue
            ruta = unquote(destino.split("#")[0])
            obj = (p.parent / ruta).resolve()
            if not obj.exists():
                h["enlaces_rotos"].append(f"{rel} -> {destino}")
            elif obj in entrantes and obj != p:
                entrantes[obj].add(p)
        for nombre, ancla in WIKILINK.findall(t):
            objs = por_nombre.get(nombre.strip().lower(), [])
            if not objs:
                h["wikilinks_rotos"].append(f"{rel} -> [[{nombre}]]")
                continue
            obj = objs[0]
            if ancla and ancla.strip().lower() not in encabezados(obj):
                h["wikilinks_rotos"].append(f"{rel} -> [[{nombre}#{ancla}]] (no existe ese encabezado)")
            if obj in entrantes and obj != p:
                entrantes[obj].add(p)
        m = re.match(r"\A---\n(.*?)\n---\n", t, flags=re.S)
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
        if p.name != "log.md":
            intro_citada = False
            for b in bloques(t):
                es_tabla = b.startswith("|")
                cita = "fuentes/" in b or bool(WIKILINK.search(b)) or bool(ENLACE_MD.search(b))
                if not es_tabla:
                    intro_citada = "fuentes/" in b
                tiene_etiqueta = any(e in b for e in ETIQUETAS)
                if CIFRA.search(b) and not tiene_etiqueta and not es_tabla and p != indice:
                    h["sin_etiqueta"].append(f"{rel}: {b[:90]!r}")
                if ("[OBSERVADO]" in b or "[CALCULADO]" in b) and not cita and not (es_tabla and intro_citada):
                    h["sin_cita"].append(f"{rel}: {b[:90]!r}")
                for frase in ("no entregó", "no proporcionó", "no se proporcionaron", "no entregaron"):
                    if frase in b.lower() and "«" not in b:
                        h["frase_prohibida"].append(f"{rel}: {frase}")
        m1 = re.search(r"^# (.+)$", t, flags=re.M)
        if m1:
            titulos.setdefault(m1.group(1).strip().lower(), []).append(rel)
    for p, desde in entrantes.items():
        if p == indice:
            continue
        if not desde:
            h["huerfanas"].append(p.relative_to(RAIZ).as_posix())
        if indice not in desde:
            h["fuera_del_indice"].append(p.relative_to(RAIZ).as_posix())
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
