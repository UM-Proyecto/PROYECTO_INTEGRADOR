"""Control positivo y negativo de src/u4-t1/salud.py sobre una wiki mínima armada en un directorio temporal."""
import os, pathlib, subprocess, sys, tempfile, unittest

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "src/u4-t1/salud.py"
META = ("---\ntipo: fuente\nfuentes: [F01]\nfecha: 2026-10-14\nestado: observado\nrevision: revisado\n"
        "actualizado: 2026-11-03\ntags: [fuente]\n---\n")


def correr(raiz):
    return subprocess.run([sys.executable, "-I", str(SCRIPT)], capture_output=True, text=True,
                          env={**os.environ, "PI_RAIZ": str(raiz)})


class TestSalud(unittest.TestCase):
    def armar(self, d, pagina):
        w = pathlib.Path(d) / "wiki"; (w / "fuentes").mkdir(parents=True)
        (pathlib.Path(d) / "fuentes").mkdir(); (pathlib.Path(d) / "fuentes/a.csv").write_text("x\n")
        (w / "index.md").write_text(META + "# Índice\n\n- [[F01-a]]\n- [[log|Registro]]\n")
        (w / "log.md").write_text(META + "# Log\n\nVer [[index]].\n")
        (w / "fuentes/F01-a.md").write_text(META + pagina)

    def test_wiki_sana_sale_cero(self):
        with tempfile.TemporaryDirectory() as d:
            self.armar(d, "# F01\n\n## Datos\n\n[OBSERVADO] Son 20 de 20 filas ([a](../../fuentes/a.csv)), "
                          "ver [[F01-a#Datos|abajo]].\n")
            r = correr(d)
            self.assertEqual(r.returncode, 0, r.stdout)

    def test_detecta_cada_falla(self):
        with tempfile.TemporaryDirectory() as d:
            self.armar(d, "# F01\n\nSon 6 de 15 componentes.\n\n[OBSERVADO] Algo sin cita.\n\n"
                          "La empresa no entregó datos.\n\n[roto](../nada.md) [[no-existe]] [[index#Nada]]\n")
            (pathlib.Path(d) / "wiki/suelta.md").write_text("# Suelta\n")
            r = correr(d)
            self.assertEqual(r.returncode, 1)
            for clave in ("enlaces_rotos: 1", "wikilinks_rotos: 2", "huerfanas: 1", "fuera_del_indice: 1",
                          "sin_metadatos: 1", "sin_etiqueta: 1", "sin_cita: 1", "frase_prohibida: 1"):
                self.assertIn(clave, r.stdout)


if __name__ == "__main__":
    unittest.main()
