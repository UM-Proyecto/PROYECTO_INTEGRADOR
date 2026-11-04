# Manifiesto de fuentes

Esta carpeta guarda copias exactas de los archivos del repositorio del equipo `UM-Proyecto/MINERIA_DATOS`, tomadas del commit `c27757a` (3 de noviembre de 2026, 13:48, rama `main`) el 3 de noviembre de 2026. Los originales siguen en el repositorio y no se modificaron. Las huellas SHA-256 y los tamaños están en `MANIFIESTO.csv`; `python3 src/u4-t1/manifiesto.py` comprueba que ninguna copia cambió desde que se incorporó.

Nada de lo que hay en `fuentes/` se edita. Si una fuente cambia en el repositorio, se copia la versión nueva en una carpeta nueva (por ejemplo `F05b_...`), se agrega al manifiesto y se registra en `wiki/log.md`.

## Cómo se clasifican los datos

El proyecto mezcla tres clases de datos y la wiki las nombra siempre igual que el registro de la HU-02 (columna `tipo_dato`):

- FICTICIO: datos de prueba armados por el equipo. MULTIPARTES facilitó una muestra inicial de unos 20 registros, y el equipo la amplió con datos de prueba con la misma estructura para poder aplicar y comparar técnicas. Sirven para probar métodos, no para describir a la empresa.
- PUBLICO: datos reales publicados por terceros (INE de Bolivia, Banco Central de Bolivia, un agente de carga, la Bolsa de Fletes de Shanghái).
- MIXTO: tablas que combinan datos públicos con datos de prueba.

## Permiso de uso

Los archivos del repositorio son trabajo académico del equipo (Sabrina Adrian Zelaya, Samuel Castillo y Fiorella Sandoval) para Minería de Datos y Business Intelligence II de la Universidad Privada del Valle, 2026. Se usan acá con fines académicos. Los datos públicos se citan con su URL. No hay datos personales: los proveedores y repuestos de los datos de prueba tienen códigos ficticios.

## Fuentes

| Código | Archivos | Qué es | Clase | Fecha o corte de los datos | Limitaciones |
|---|---|---|---|---|---|
| F01 | `PREGUNTA ENFOCADA Y OBJETIVO.docx` | Pregunta enfocada y objetivo general del proyecto, redactados por Fiorella Sandoval (SCRUM-37) | Descripción del objetivo, no son datos | 14-oct-2026 | Escribe el nombre como «MULTIPARTE» en el objetivo y «MULTIPARTES» en la pregunta. No fija usuario ni decisión concretos; eso lo agregan los documentos de la HU-34 y la HU-33 |
| F02 | `registro_actualizaciones.csv`, `conjuntos.csv`, `historial_cargas.csv`, `LEEME.md` | Registro de origen, responsable, fecha de corte y huella de cada conjunto de datos (HU-02, SCRUM-12, Samuel) | Metadatos de 17 conjuntos: 13 FICTICIO, 3 PUBLICO, 1 MIXTO | Cargas del 27-oct-2026 18:00 UTC | Es un registro, no los datos. Las fechas de corte de distintos conjuntos no coinciden entre sí |
| F03 | `CRITERIOS_APROBADOS.md`, `BORRADOR_criterios_exito.md` | Los tres criterios de éxito aprobados por el equipo el 27-oct-2026 y el borrador con cinco candidatos (HU-33, SCRUM-44, Samuel) | Definición de indicadores y resultados esperados | Líneas base medidas el 26-oct-2026 | Las metas (15 %, 80 %, 30 días) las propuso el equipo; no salen de una norma ni de un estándar |
| F04 | `comparacion_pronosticos.csv`, `README.md` | Comparación de tres métodos de pronóstico de salidas en 10 repuestos con MAE (HU-07, SCRUM-20, Fiorella) | FICTICIO | Evaluación del 10 al 14-sep-2026 | Sólo dos semanas de historial; ningún método queda elegible. La repetición con 284 días (HU-36, SCRUM-47) está comentada en Jira y no está en el repositorio |
| F05 | `hu31_costos_importacion.csv`, `flete_referencias_puntuales.csv`, `SHA256SUMS_insumos_publicos.txt`, `LEEME_hu30-31.md` | Componentes del costo de importar repuestos desde China, cada uno marcado DOCUMENTADO, ESTIMACION o PENDIENTE (HU-31, SCRUM-7, Samuel) | MIXTO (la tabla de costos) y PUBLICO (las referencias de flete) | Corte 2026-10-09 (SCFI); cotizaciones de junio de 2026; INE 2025-09 a 2026-08 | Las cotizaciones son indicativas y públicas, no la tarifa que pagaría MULTIPARTES. La URL de descarga del INE no está en el repositorio |
| F06 | `README.md` | Portada del repositorio: historias de usuario, responsables, origen de los datos y criterios de éxito | Documento del equipo | Commit `c27757a`, 3-nov-2026 | Resume a las otras fuentes; ante una diferencia manda el archivo de origen |
| F07 | `HU34_Descripcion_Datos_MULTIPARTE.md`, `ventas_simuladas.csv`, `Guia_Limpieza.md` | Descripción de los tres conjuntos simulados de la HU-34 (ventas, compras e inventario), las ventas diarias por repuesto y la guía de limpieza (HU-34, SCRUM-45 y SCRUM-50, Fiorella). Incorporada el 3-nov-2026 para la segunda ingesta | FICTICIO | Ventas del 2025-01-01 al 2026-10-24 | Los datos son de prueba. La descripción usa una redacción sobre los datos de la empresa distinta de la de F06. Los códigos de repuesto (`sku`) no siguen el formato de los de F04 |
