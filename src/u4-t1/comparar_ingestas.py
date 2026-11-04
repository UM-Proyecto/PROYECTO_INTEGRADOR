"""Compara la wiki en dos commits: páginas, wikilinks, citas a fuentes, contradicciones y páginas que citan cada fuente.

Uso:  python3 src/u4-t1/comparar_ingestas.py <commit_antes> <commit_despues>
Ejemplo (segunda ingesta): python3 src/u4-t1/comparar_ingestas.py 758489d HEAD
"""
import re, subprocess, sys

WIKILINK = re.compile(r"\[\[([^\]|#]+)")
CITA = re.compile(r"\]\((?:\.\./)+fuentes/(F\d\d)")


def git(*a):
    return subprocess.run(["git", *a], capture_output=True, text=True, check=True).stdout


def foto(commit):
    pags = [p for p in git("ls-tree", "-r", "--name-only", commit, "wiki/").split() if p.endswith(".md")]
    wl = citas = 0
    por_fuente, contr = {}, set()
    for p in pags:
        t = git("show", f"{commit}:{p}")
        wl += len(WIKILINK.findall(t))
        cs = CITA.findall(t)
        citas += len(cs)
        for f in set(cs):
            por_fuente.setdefault(f, set()).add(p)
        if p == "wiki/index.md":
            contr = set(re.findall(r"^\| (C-\d\d) ", t, flags=re.M))
    return pags, wl, citas, por_fuente, contr


a, b = sys.argv[1], sys.argv[2]
pa, wa, ca, fa, xa = foto(a)
pb, wb, cb, fb, xb = foto(b)
print(f"páginas: {len(pa)} -> {len(pb)}; nuevas: {sorted(set(pb) - set(pa))}")
print(f"wikilinks: {wa} -> {wb}")
print(f"citas a fuentes/: {ca} -> {cb}")
print(f"contradicciones en el índice: {sorted(xa)} -> {sorted(xb)}")
cambiadas = [p for p in sorted(set(pa) & set(pb))
             if subprocess.run(["git", "diff", "--quiet", a, b, "--", p]).returncode != 0]
print(f"páginas modificadas: {len(cambiadas)}: {cambiadas}")
for f in sorted(set(fa) | set(fb)):
    print(f"  páginas que citan {f}: {len(fa.get(f, ()))} -> {len(fb.get(f, ()))}")
