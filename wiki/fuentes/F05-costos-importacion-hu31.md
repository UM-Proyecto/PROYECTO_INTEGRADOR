---
tipo: fuente
subtipo: fuente
fuentes: [F05, F02, F06]
fecha: 2026-10-09
clase_datos: [MIXTO, PUBLICO]
estado: observado
revision: borrador
actualizado: 2026-11-03
tags: [fuente, mixto, publico]
---

# F05. Costos de importación (HU-31)

**Archivos:** [`hu31_costos_importacion.csv`](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv) (15 componentes del costo con su respaldo), [`flete_referencias_puntuales.csv`](../../fuentes/F05_costos_importacion_HU31/flete_referencias_puntuales.csv) (6 referencias públicas de flete), [`SHA256SUMS_insumos_publicos.txt`](../../fuentes/F05_costos_importacion_HU31/SHA256SUMS_insumos_publicos.txt) y [`LEEME_hu30-31.md`](../../fuentes/F05_costos_importacion_HU31/LEEME_hu30-31.md). **Historia:** HU-31, SCRUM-7, Samuel Castillo.

**Clase:** la tabla de costos es MIXTO y las referencias de flete son PUBLICO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `costos_importacion` y `flete_referencias`). Ver C-04 y C-05 abajo.

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

- [OBSERVADO] Las cotizaciones son indicativas y públicas, no la tarifa que pagaría MULTIPARTES; la URL de descarga del INE no está en el repositorio ([manifiesto](../../fuentes/MANIFIESTO.md), fila F05).
- [INFERENCIA] Las cotizaciones del agente de carga tienen fecha 2026-06: al 3-nov-2026 tienen unos cinco meses. La nota dice que la página se modificó el 2026-06-02.
- [OBSERVADO] Las rutas South America (Santos) y WCSA (Manzanillo) del SCFI «vienen en null sin registro» ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), fila `indice compuesto SCFI`, columna `nota`). El índice que se usa es el compuesto mundial, no una ruta a Sudamérica.

## Contradicciones

- **C-04. Qué tiene de FICTICIO la tabla de costos (resuelta en la revisión 01).** [OBSERVADO] F02 registra `costos_importacion` como MIXTO y describe su origen como «Referencias públicas de flete y estimaciones de HU-31» ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`, columna `fuente`). F06 dice «MIXTO: fletes públicos (INE, agente de carga, SCFI) y cotizaciones de proveedor FICTICIAS» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla de historias, fila HU-31), pero esa fila describe la **historia** HU-31 entera, que tiene tres conjuntos: esta tabla, `cotizaciones_proveedor` y `costos_complementarios`; los dos últimos, FICTICIOS ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `cotizaciones_proveedor` y `costos_complementarios`). [INFERENCIA] No es una contradicción entre fuentes. La tabla no trae datos FICTICIOS: es MIXTO porque combina valores publicados (6 DOCUMENTADO) con estimaciones calculadas sobre datos públicos del INE (5 ESTIMACION), y las 4 filas PENDIENTE no tienen valor. La primera versión de esta página, escrita por el agente, la dejó como contradicción pendiente porque leyó la fila de F06 como si describiera sólo la tabla; la revisión 01 la corrigió. La revisión de salud R-01 corrigió «dos conjuntos» por «tres» y puso en duda el motivo del MIXTO (C-05, abajo).
- **C-05. Por qué la tabla de costos es MIXTO (pendiente).** [OBSERVADO] El manifiesto define MIXTO como «tablas que combinan datos públicos con datos de prueba» ([manifiesto](../../fuentes/MANIFIESTO.md), «Cómo se clasifican los datos»), y F06 dice que los costos de la HU-31 «combinan las fuentes públicas con datos FICTICIOS de la empresa» ([F06](../../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»). La tabla no tiene ninguna fila de datos de prueba: 6 valores publicados, 5 estimaciones sobre datos del INE y 4 filas vacías ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `tipo_dato` y `respaldo`). F02 la registra como MIXTO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`). [INFERENCIA] Para la clase prevalece F02 y la wiki sigue diciendo MIXTO. Pero el motivo que dio la resolución de C-04 («publicados más estimaciones») no sale de ninguna fuente, y con la definición del manifiesto la tabla sería PUBLICO. **Pendiente** de que el equipo (Samuel Castillo, responsable del conjunto) diga si F02 debe decir PUBLICO o si cuenta las estimaciones de la HU-31 como dato propio. No cambia el valor de [[KPI-2-costo-con-respaldo|KPI-2]]. Detalle en [[R-01-salud-3-nov#H-02. Qué hace MIXTA a la tabla de costos (C-05)|R-01]].

## Cómo recalcular

    python3 -c "import csv,collections;k=list(csv.DictReader(open('fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv',encoding='utf-8')));print(len(k),collections.Counter(x['tipo_dato'] for x in k),collections.Counter(bool(x['respaldo']) for x in k))"

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: en C-04, «dos conjuntos» pasó a «tres» (H-03); se agregó C-05 (H-02).
