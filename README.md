# Proyecto Integrador: apoyo a las decisiones de compra de MULTIPARTES

Proyecto Integrador (Universidad Privada del Valle, VI semestre, 2026), trabajado desde Business Intelligence II. Equipo: Sabrina Adrian Zelaya, Samuel Castillo y Fiorella Sandoval. El proyecto de Minería de Datos sobre la misma empresa vive en [`UM-Proyecto/MINERIA_DATOS`](https://github.com/UM-Proyecto/MINERIA_DATOS); de ahí salen las fuentes de este repositorio, copiadas con su commit de origen y su huella.

**Pregunta enfocada.** ¿Qué técnicas de análisis de datos permiten apoyar las decisiones de compra de la empresa MULTIPARTES de Santa Cruz de la Sierra durante el segundo semestre de 2026?

## De dónde salen los datos

- Las fuentes están en [`fuentes/`](fuentes/), copiadas del commit `c27757a` de `MINERIA_DATOS` el 3 de noviembre de 2026. [`fuentes/MANIFIESTO.md`](fuentes/MANIFIESTO.md) dice qué es cada una, su fecha, su permiso de uso y sus límites, y `fuentes/MANIFIESTO.csv` guarda la huella SHA-256 de cada archivo.
- **FICTICIOS:** movimientos de inventario, stock, catálogo, ventas, compras y pronósticos. MULTIPARTES facilitó una muestra inicial de unos 20 registros; el equipo la amplió con datos de prueba con la misma estructura.
- **PÚBLICOS y reales:** fletes de importación (INE de Bolivia, cotizaciones de un agente de carga, índice SCFI de Shanghái).
- **MIXTOS:** los costos de importación de la HU-31.

## Tareas

| Tarea | Materia | Qué hace | Documentos | Código | Wiki | Informe |
|---|---|---|---|---|---|---|
| U4-T1 | Business Intelligence II | Wiki de conocimiento mantenida con un agente de IA (patrón LLM Wiki): fuentes, indicadores, consulta verificada, revisión de salud y segunda ingesta | [`docs/u4-t1`](docs/u4-t1) | [`src/u4-t1`](src/u4-t1) | [`wiki/index.md`](wiki/index.md) | [`reports/u4-t1`](reports/u4-t1) |

## Estructura

```text
fuentes/      copias intactas de las fuentes, con MANIFIESTO.md y MANIFIESTO.csv
wiki/         la wiki: index.md, log.md, objetivos, fuentes, indicadores, síntesis, consultas y revisiones
AGENTS.md     instrucciones para el agente que mantiene la wiki
data/
  raw/        datos fuente nuevos que no vengan de MINERIA_DATOS
  processed/  resultados generados por los scripts de src/
docs/         prompts y evidencia de cada corrida del agente y de su revisión, por tarea
src/          scripts de verificación y de corrida del agente, por tarea
tests/        pruebas
reports/      informes entregados, por tarea
notebooks/    cuadernos
```

## Cómo reproducir las verificaciones

Con Python 3.10 o superior y sólo la biblioteca estándar:

```bash
python3 src/u4-t1/manifiesto.py                       # las fuentes no cambiaron
python3 -m unittest discover -s tests -p "test_*.py"  # pruebas
```

Las demás verificaciones de la U4-T1 se documentan en [`docs/u4-t1/REPRODUCIR.md`](docs/u4-t1/REPRODUCIR.md).
