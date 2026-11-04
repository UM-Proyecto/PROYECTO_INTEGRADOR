"""Convierte wiki/ al formato Obsidian sin perder la lectura en GitHub.

Uso:  python3 src/u4-t1/obsidian.py [--revisar]   (--revisar: sólo informa, no escribe)

Qué hace en cada página de wiki/:
  - Enlace Markdown a otra página de la wiki o a AGENTS.md  ->  [[nombre#Encabezado|texto]].
    El ancla se traduce al texto real del encabezado, que es lo que Obsidian resuelve.
  - Enlaces a fuentes/ y a otros archivos que no son páginas: quedan como enlace Markdown relativo,
    que Obsidian y GitHub resuelven los dos.
  - Metadatos: tipo pasa a la familia del gráfico (fuente, indicador, hallazgo, decision, mapa,
    registro) y el valor original queda en subtipo; fecha_datos pasa a fecha; el estado de revisión
    (borrador, revisado, pendiente) pasa a revision; estado pasa a ser la naturaleza del contenido
    (observado, inferido, supuesto o esperado); se agregan tags con la familia y las clases de datos.
Es idempotente: una página ya convertida no cambia.
"""
import pathlib, re, sys
from urllib.parse import unquote

RAIZ = pathlib.Path(__file__).resolve().parents[2]
WIKI = RAIZ / "wiki"
FAMILIA = {"fuente": "fuente", "indicador": "indicador", "sintesis": "hallazgo", "consulta": "hallazgo",
           "revision": "hallazgo", "mapa": "decision", "objetivos": "decision", "indice": "mapa", "log": "registro"}
NATURALEZA = {"fuente": "observado", "indicador": "esperado", "hallazgo": "inferido", "decision": "esperado",
              "mapa": "observado", "registro": "observado"}
ENLACE = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)\s]+)\)")


def slug(t):
    t = re.sub(r"[^\w\s-]", "", t.strip().lower())
    return re.sub(r"\s+", "-", t)


def encabezados(p):
    return {slug(h): h.strip() for h in re.findall(r"^#{1,6} (.+)$", p.read_text(encoding="utf-8"), flags=re.M)}


def convertir_enlaces(p, t):
    def rep(m):
        texto, destino = m.group(1), m.group(2)
        if re.match(r"^[a-z]+://|^mailto:|^#", destino):
            return m.group(0)
        ruta, _, ancla = destino.partition("#")
        obj = (p.parent / unquote(ruta)).resolve()
        if obj.suffix != ".md" or not obj.exists() or not (WIKI in obj.parents or obj == RAIZ / "AGENTS.md"):
            return m.group(0)
        nombre = obj.stem
        if ancla:
            h = encabezados(obj).get(slug(unquote(ancla)), unquote(ancla))
            nombre += "#" + h
        texto_limpio = texto.strip("`")
        if texto_limpio in (obj.stem, obj.name):
            return f"[[{nombre}]]"
        return f"[[{nombre}|{texto}]]"
    return ENLACE.sub(rep, t)


def convertir_meta(t):
    m = re.match(r"\A---\n(.*?)\n---\n", t, flags=re.S)
    if not m or re.search(r"^subtipo:", m.group(1), flags=re.M):
        return t
    meta = m.group(1)
    def valor(campo):
        v = re.search(rf"^{campo}:\s*(.*)$", meta, flags=re.M)
        return v.group(1).split("#")[0].strip() if v else ""
    tipo = valor("tipo")
    fam = FAMILIA.get(tipo, tipo)
    clases = [c.strip().lower() for c in valor("clase_datos").strip("[]").split(",") if c.strip()]
    rev = valor("estado")
    lineas = []
    for l in meta.split("\n"):
        if l.startswith("tipo:"):
            lineas += [f"tipo: {fam}", f"subtipo: {tipo}"]
        elif l.startswith("fecha_datos:"):
            lineas.append("fecha:" + l[len("fecha_datos:"):])
        elif l.startswith("estado:"):
            lineas += [f"estado: {NATURALEZA.get(fam, 'observado')}", f"revision: {rev}"]
        else:
            lineas.append(l)
    tags = [fam] + clases + (["moc"] if fam == "mapa" else [])
    lineas.append("tags: [" + ", ".join(dict.fromkeys(tags)) + "]")
    return "---\n" + "\n".join(lineas) + "\n---\n" + t[m.end():]


def main():
    cambios = 0
    for p in sorted(WIKI.rglob("*.md")):
        t = p.read_text(encoding="utf-8")
        n = convertir_enlaces(p, convertir_meta(t))
        if n != t:
            cambios += 1
            print("convertida", p.relative_to(RAIZ))
            if "--revisar" not in sys.argv:
                p.write_text(n, encoding="utf-8")
    print(f"{cambios} páginas {'por convertir' if '--revisar' in sys.argv else 'convertidas'}")


if __name__ == "__main__":
    main()
