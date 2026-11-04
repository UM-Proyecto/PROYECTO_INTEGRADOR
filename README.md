# Proyecto Integrador: apoyo a las decisiones de compra de MULTIPARTES

Proyecto Integrador de la Universidad Privada del Valle (VI semestre, 2026), trabajado desde Business Intelligence II.

**La empresa.** MULTIPARTES es una importadora de repuestos automotrices de Santa Cruz de la Sierra que compra a proveedores de China. Quien usa los resultados es su jefe de compras, que decide qué repuesto pedir, en qué cantidad y cuándo.

**La pregunta enfocada.** ¿Qué técnicas de análisis de datos permiten apoyar las decisiones de compra de la empresa MULTIPARTES de Santa Cruz de la Sierra durante el segundo semestre de 2026?

**El equipo.** Sabrina Adrian Zelaya, Samuel Castillo y Fiorella Sandoval.

**De dónde viene.** El trabajo de datos se hace en el proyecto de Minería de Datos sobre la misma empresa, [`UM-Proyecto/MINERIA_DATOS`](https://github.com/UM-Proyecto/MINERIA_DATOS). Este repositorio no lo duplica: copia de ahí las fuentes que usa, con el commit de origen y la huella de cada archivo, y construye sobre ellas la wiki de conocimiento del proyecto.

## Por dónde empezar

1. [`wiki/index.md`](wiki/index.md) es el mapa de la wiki: fuentes, indicadores, síntesis por objetivo, consultas, revisiones y la tabla de contradicciones.
2. [`wiki/objetivos.md`](wiki/objetivos.md) conecta cada objetivo con su fuente, su indicador, su página y la decisión que apoya.
3. [`reports/u4-t1`](reports/u4-t1) tiene el informe de la tarea U4-T1, en Word y PDF.
4. [`wiki/log.md`](wiki/log.md) cuenta, en orden, qué hizo el agente de IA en cada etapa y qué corrigió la revisión humana.

## Tareas

| Tarea | Materia | Qué hace | Wiki | Prompts y evidencia | Código | Informe |
|---|---|---|---|---|---|---|
| U4-T1 | Business Intelligence II | Wiki de conocimiento mantenida con un agente de IA (patrón LLM Wiki de Karpathy): fuentes conservadas, indicadores definidos, consulta verificada, revisión de salud y segunda ingesta | [`wiki/index.md`](wiki/index.md) | [`docs/u4-t1`](docs/u4-t1) | [`src/u4-t1`](src/u4-t1) | [`reports/u4-t1`](reports/u4-t1) |

## Cómo está organizado

```text
fuentes/      copias intactas de las fuentes, con MANIFIESTO.md (procedencia, fecha, permiso, límites)
              y MANIFIESTO.csv (commit de origen, ruta original y sha256 de cada archivo)
wiki/         la wiki: index.md (mapa), log.md, objetivos.md, fuentes/, indicadores/, sintesis/,
              consultas/ y revisiones/
AGENTS.md     instrucciones para el agente que mantiene la wiki: estructura, formato, citas,
              contradicciones, privacidad y compatibilidad con Obsidian
.obsidian/    configuración mínima para abrir el repositorio como bóveda de Obsidian
data/
  raw/        datos fuente nuevos que no vengan de MINERIA_DATOS (hoy vacía)
  processed/  resultados de los scripts de verificación
docs/u4-t1/   prompts inicial y mejorado, explicación de los cambios, y la evidencia de cada
              corrida del agente (prompt, transcripción, respuesta) y de cada revisión humana
src/u4-t1/    scripts: manifiesto, verificación de cifras, revisión de salud, conversión a
              Obsidian y corrida del agente
tests/        pruebas de los scripts, con controles positivos y negativos
reports/      informes entregados, por tarea
notebooks/    cuadernos (hoy vacía)
```

## De dónde salen los datos

Las fuentes están copiadas en [`fuentes/`](fuentes/) desde el commit `c27757a` de `MINERIA_DATOS`, tomadas el 3 de noviembre de 2026. Los datos se nombran igual que en el registro de fuentes del proyecto:

- **FICTICIO:** movimientos de inventario, stock, catálogo, ventas, compras y pronósticos. MULTIPARTES facilitó una muestra inicial de unos 20 registros, y el equipo la amplió con datos de prueba con la misma estructura para poder aplicar y comparar técnicas. Un resultado sobre estos datos prueba un método, no describe a la empresa.
- **PUBLICO:** fletes de importación (INE de Bolivia, cotizaciones de un agente de carga, índice SCFI de Shanghái).
- **MIXTO:** la tabla de costos de importación, que combina valores publicados con estimaciones calculadas sobre datos del INE.

## Cómo abrir la wiki

**En GitHub.** Se lee directamente: entrar a [`wiki/index.md`](wiki/index.md). Las citas a las fuentes son enlaces que abren el archivo. Los enlaces entre páginas aparecen como `[[nombre de página]]`: la página está en `wiki/` con ese nombre y la extensión `.md`.

**En Obsidian.** Así se ven los enlaces entre páginas y el gráfico.

1. Clonar el repositorio: `git clone https://github.com/UM-Proyecto/PROYECTO_INTEGRADOR.git`
2. En Obsidian, «Abrir carpeta como bóveda» y elegir la carpeta `PROYECTO_INTEGRADOR` entera, no sólo `wiki/`. Así resuelven también las citas a `fuentes/`.
3. Si Obsidian pregunta, confiar en la bóveda. No necesita plugins de la comunidad.
4. Abrir `wiki/index.md`, que es el mapa de contenidos.
5. Abrir la vista de gráfico (Ctrl+G o Cmd+G). Ya viene filtrada a `wiki/` y coloreada por tipo de página: azul para fuentes, naranja para indicadores, verde para hallazgos (síntesis, consultas y revisiones), rojo para decisiones (el mapa de objetivos), violeta para el índice y gris para el registro.

Cada página tiene metadatos que Obsidian muestra como propiedades: `tipo`, `fuentes`, `fecha` de los datos, `estado` (observado, inferido, supuesto o esperado), `revision` y `tags`.

## Cómo reproducir las verificaciones

Con Python 3.10 o superior y sólo la biblioteca estándar, desde la raíz del repositorio:

```bash
python3 src/u4-t1/manifiesto.py                       # las copias de fuentes/ no cambiaron
python3 src/u4-t1/verificar.py                        # recalcula desde fuentes/ las cifras que afirma la wiki
python3 src/u4-t1/salud.py                            # enlaces, wikilinks, huérfanas, metadatos, citas
python3 -m unittest discover -s tests -p "test_*.py"  # pruebas, con controles negativos
```

Cada script sale con código 1 si encuentra un problema. El detalle de qué comprueba cada uno, y cómo se repite una corrida del agente, está en [`docs/u4-t1/REPRODUCIR.md`](docs/u4-t1/REPRODUCIR.md).
