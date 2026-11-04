"""Control positivo y negativo de src/u4-t1/salud.py sobre una wiki mínima armada en un directorio temporal."""
import os, pathlib, subprocess, sys, tempfile, unittest

SCRIPT = pathlib.Path(__file__).resolve().parent.parent / "src/u4-t1/salud.py"
META = "---\ntipo: fuente\nfuentes: [F01]\nfecha_datos: 2026-10-14\nestado: revisado\nactualizado: 2026-11-03\n---\n"


def correr(raiz):
    return subprocess.run([sys.executable, "-I", str(SCRIPT)], capture_output=True, text=True,
                          env={**os.environ, "PI_RAIZ": str(raiz)})


class TestSalud(unittest.TestCase):
    def armar(self, d, pagina):
        w = pathlib.Path(d) / "wiki"; (w / "fuentes").mkdir(parents=True)
        (pathlib.Path(d) / "fuentes").mkdir(); (pathlib.Path(d) / "fuentes/a.csv").write_text("x\n")
        (w / "index.md").write_text("# Índice\n\n- [F01](fuentes/F01.md)\n- [Log](log.md)\n")
        (w / "log.md").write_text("# Log\n")
        (w / "fuentes/F01.md").write_text(META + pagina)

    def test_wiki_sana_sale_cero(self):
        with tempfile.TemporaryDirectory() as d:
            self.armar(d, "# F01\n\n[OBSERVADO] Son 20 de 20 filas ([a](../../fuentes/a.csv)).\n")
            r = correr(d)
            self.assertEqual(r.returncode, 0, r.stdout)

    def test_detecta_cada_falla(self):
        with tempfile.TemporaryDirectory() as d:
            self.armar(d, "# F01\n\nSon 6 de 15 componentes.\n\n[OBSERVADO] Algo sin cita.\n\n"
                          "La empresa no entregó datos.\n\n[roto](../nada.md)\n")
            (pathlib.Path(d) / "wiki/suelta.md").write_text("# Suelta\n")
            r = correr(d)
            self.assertEqual(r.returncode, 1)
            for clave in ("enlaces_rotos: 1", "huerfanas: 1", "sin_metadatos: 1", "sin_etiqueta: 1",
                          "sin_cita: 1", "frase_prohibida: 1"):
                self.assertIn(clave, r.stdout)


if __name__ == "__main__":
    unittest.main()
