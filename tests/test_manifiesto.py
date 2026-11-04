"""Comprueba que las copias de fuentes/ siguen idénticas a las registradas en MANIFIESTO.csv.

python3 -m unittest discover -s tests -p "test_*.py"
"""
import subprocess, sys, pathlib, unittest

RAIZ = pathlib.Path(__file__).resolve().parent.parent


class TestManifiesto(unittest.TestCase):
    def test_fuentes_intactas(self):
        r = subprocess.run([sys.executable, "-I", str(RAIZ / "src/u4-t1/manifiesto.py")],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("copias intactas", r.stdout)


if __name__ == "__main__":
    unittest.main()
