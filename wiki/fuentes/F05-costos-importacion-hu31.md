---
tipo: fuente
fuentes: [F05, F02, F06]
fecha_datos: 2026-10-09
clase_datos: [MIXTO, PUBLICO]
estado: revisado
actualizado: 2026-11-03
---

# F05. Costos de importación (HU-31)

**Archivos:** [`hu31_costos_importacion.csv`](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv) (15 componentes del costo con su respaldo), [`flete_referencias_puntuales.csv`](../../fuentes/F05_costos_importacion_HU31/flete_referencias_puntuales.csv) (6 referencias públicas de flete), [`SHA256SUMS_insumos_publicos.txt`](../../fuentes/F05_costos_importacion_HU31/SHA256SUMS_insumos_publicos.txt) y [`LEEME_hu30-31.md`](../../fuentes/F05_costos_importacion_HU31/LEEME_hu30-31.md). **Historia:** HU-31, SCRUM-7, Samuel Castillo.

**Clase:** la tabla de costos es MIXTO y las referencias de flete son PUBLICO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `costos_importacion` y `flete_referencias`). Ver C-04 abajo.

> Atención al nombre de columna: en `hu31_costos_importacion.csv` la columna `tipo_dato` no guarda la clase (FICTICIO, PUBLICO, MIXTO) sino el **respaldo**: DOCUMENTADO, ESTIMACION o PENDIENTE. En la wiki se llama «respaldo».

## Qué dice

- [CALCULADO] La tabla tiene 15 componentes: 6 DOCUMENTADO, 5 ESTIMACION y 4 PENDIENTE ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`). Coincide con la línea base de F03.
- [OBSERVADO] Los 6 DOCUMENTADO son cinco cotizaciones indicativas de un agente de carga (FCL 20 y 40 pies, LCL, aéreo y express, fechadas 2026-06) y el índice compuesto SCFI de Shanghái al 2026-10-09 ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `concepto`, `fecha_dato` y `nota`). La nota de las cinco cotizaciones dice «cotizacion indicativa de proveedor (secundaria)».
- [OBSERVADO] Los 5 ESTIMACION son el flete y seguro implícito (CIF menos FOB) de importaciones desde China de 10 partidas de repuestos, uno por medio de transporte (aéreo, carretera, courier, ferroviario y postal), calculados sobre datos del INE de 2025-09 a 2026-08. La nota aclara: «agregado declarado en aduana, no tarifa cotizada; flete y seguro vienen juntos» ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`).
- [OBSERVADO] Los 4 PENDIENTE son seguro separado del flete, nacionalización y agente aduanero, comisiones de gestión y flete terrestre de Arica o Iquique a Santa Cruz. Los cuatro dicen «sin documento de respaldo en las fuentes disponibles; pedir facturas al encargado de compras» ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`).
- [OBSERVADO] Las 6 referencias de `flete_referencias_puntuales.csv` son las mismas 6 filas DOCUMENTADO de la tabla de costos, con su URL ([F05](../../fuentes/F05_costos_importacion_HU31/flete_referencias_puntuales.csv), columnas `concepto` y `url`).
- [OBSERVADO] Los precios, cantidades y porcentajes de los datos ficticios de la HU-30 y la HU-31 «no representan a MULTIPARTES» ([F05](../../fuentes/F05_costos_importacion_HU31/LEEME_hu30-31.md), último párrafo).
- [OBSERVADO] El archivo del INE (`ine_repuestos_flete_implicito_mensual.csv`) aparece en las huellas pero no se copió a `fuentes/` ([F05](../../fuentes/F05_costos_importacion_HU31/SHA256SUMS_insumos_publicos.txt)). Las 5 estimaciones no se pueden recalcular desde la wiki; sólo se pueden leer.

## Límites

- [OBSERVADO] Las cotizaciones son indicativas y públicas, no la tarifa que pagaría MULTIPARTES; la URL de descarga del INE no está en el repositorio (manifiesto, fila F05).
- [INFERENCIA] Las cotizaciones del agente de carga tienen fecha 2026-06: al 3-nov-2026 tienen unos cinco meses. La nota dice que la página se modificó el 2026-06-02.
- [OBSERVADO] Las rutas South America (Santos) y WCSA (Manzanillo) del SCFI «vienen en null sin registro» ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), fila `indice compuesto SCFI`, columna `nota`). El índice que se usa es el compuesto mundial, no una ruta a Sudamérica.

## Contradicciones

- **C-04. Qué tiene de FICTICIO la tabla de costos.** [OBSERVADO] F02 registra `costos_importacion` como MIXTO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`). F06 explica el MIXTO así: «fletes públicos (INE, agente de carga, SCFI) y cotizaciones de proveedor FICTICIAS» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla de historias, fila HU-31). Pero ninguna de las 15 filas de la tabla copiada trae una cotización de proveedor: 11 tienen respaldo público (URL o INE) y 4 están vacías ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `respaldo`) [CALCULADO]. Las cotizaciones FICTICIAS están en otro conjunto, `cotizaciones_proveedor` ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `cotizaciones_proveedor`). **Resolución:** la wiki sigue llamando MIXTO a la tabla, porque la clase de un conjunto la fija F02; anota que los valores copiados vienen de fuentes públicas y que la parte FICTICIA no está en esta tabla. **Pendiente** que el responsable de la HU-31 confirme si la clase debe ser PUBLICO o si falta una parte de la tabla.

## Cómo recalcular

    python3 -c "import csv,collections;k=list(csv.DictReader(open('fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv',encoding='utf-8')));print(len(k),collections.Counter(x['tipo_dato'] for x in k),collections.Counter(bool(x['respaldo']) for x in k))"
