---
tipo: indice
fuentes: [F01, F02, F03, F04, F05, F06]
fecha_datos: 2026-10-27
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: borrador
actualizado: 2026-11-03
---

# Wiki del proyecto BI de MULTIPARTES

Wiki de conocimiento para apoyar la decisión de compra de MULTIPARTES: qué repuesto pedir a China, en qué cantidad y cuándo. Las reglas para mantenerla están en [AGENTS.md](../AGENTS.md); las fuentes, en [`fuentes/MANIFIESTO.md`](../fuentes/MANIFIESTO.md).

Clases de datos (nombres del registro de la HU-02): FICTICIO (datos de prueba del equipo, a partir de una muestra inicial de unos 20 registros que facilitó MULTIPARTES), PUBLICO y MIXTO. Un número calculado sobre datos FICTICIOS prueba un método; no describe a la empresa.

## Páginas

### Generales

- [objetivos.md](objetivos.md): mapa objetivo, fuente, indicador, página y decisión, con el valor de cada indicador al 3-nov-2026.
- [log.md](log.md): registro cronológico de las etapas.

### Fuentes

- [F01. Pregunta enfocada y objetivo](fuentes/F01-pregunta-enfocada.md): pregunta y objetivo general del proyecto (docx, 14-oct-2026). Sin datos.
- [F02. Registro de fuentes y fechas (HU-02)](fuentes/F02-registro-fuentes-hu02.md): diccionario de los 17 conjuntos con clase y fecha de corte. FICTICIO, PUBLICO y MIXTO.
- [F03. Criterios de éxito (HU-33)](fuentes/F03-criterios-exito-hu33.md): definición, meta y línea base de los tres indicadores, aprobados el 27-oct-2026.
- [F04. Comparación de pronósticos (HU-07)](fuentes/F04-pronosticos-hu07.md): MAE de tres métodos en 10 repuestos, 10 al 14-sep-2026. FICTICIO.
- [F05. Costos de importación (HU-31)](fuentes/F05-costos-importacion-hu31.md): 15 componentes del costo con su respaldo, corte 2026-10-09. MIXTO y PUBLICO.
- [F06. Portada del repositorio](fuentes/F06-portada-repositorio.md): resumen del equipo sobre origen de datos, historias y criterios (commit `c27757a`).

### Indicadores

- [KPI-1. Mejora del MAE frente a «último periodo»](indicadores/KPI-1-mejora-mae-pronostico.md): meta ≥ 15 %; no medible al 3-nov-2026. FICTICIO.
- [KPI-2. Componentes del costo con respaldo](indicadores/KPI-2-costo-con-respaldo.md): meta ≥ 80 %; 40 % al 3-nov-2026. MIXTO.
- [KPI-3. Días entre el corte de movimientos y la decisión](indicadores/KPI-3-vigencia-datos.md): meta ≤ 30 días; 50 días al 3-nov-2026. FICTICIO.

### Síntesis por objetivo

- [O1. Cuánto se va a vender](sintesis/O-1-cuanto-se-vendera.md): pronóstico de salidas; sin técnica recomendable todavía.
- [O2. Cuánto cuesta traerlo](sintesis/O-2-cuanto-cuesta-traerlo.md): costo de importación; flete principal con referencias públicas, faltan los costos de llegada y nacionalización.
- [O3. Con datos al día](sintesis/O-3-datos-al-dia.md): vigencia de los datos; el registro existe, el corte de movimientos está atrasado.

### Consultas

Todavía no hay (etapa 2).

### Revisiones

Todavía no hay (etapa 3).

## Contradicciones

| Código | Entre | Qué no coincide | Resolución | Página |
|---|---|---|---|---|
| C-01 | F01 y F06 | El objetivo de F01 dice «MULTIPARTE»; la pregunta de F01 y F06 dicen «MULTIPARTES» ([F01](../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), [F06](../fuentes/F06_portada_repositorio/README.md)) | Prevalece «MULTIPARTES»; parece errata | [F01](fuentes/F01-pregunta-enfocada.md#contradicciones) |
| C-02 | F03 y F04 | Historial para el pronóstico: un año + 3 meses reservados ([F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1) frente a 12 meses + 12 meses ([F04](../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo) | Para medir KPI-1 prevalece F03 (criterio aprobado, posterior). **Pendiente** que el equipo alinee la regla de selección | [KPI-1](indicadores/KPI-1-mejora-mae-pronostico.md#contradicciones) |
| C-03 | F02 y F06 | HU-32: MIXTO en F06; su conjunto `tc_series_diaria` es PUBLICO en F02 ([F06](../fuentes/F06_portada_repositorio/README.md), fila HU-32; [F02](../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `tc_series_diaria`) | Prevalece F02 para la clase del conjunto. **Pendiente** si falta registrar la parte FICTICIA | [F02](fuentes/F02-registro-fuentes-hu02.md#contradicciones) |
| C-04 | F02, F05 y F06 | La tabla de costos es MIXTO por «cotizaciones de proveedor FICTICIAS» según F06, pero sus 15 filas no traen ninguna ([F06](../fuentes/F06_portada_repositorio/README.md), fila HU-31; [F05](../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `respaldo`) | Se mantiene MIXTO (lo fija F02) con la aclaración. **Pendiente** confirmación del responsable de la HU-31 | [F05](fuentes/F05-costos-importacion-hu31.md#contradicciones) |

## Ambigüedades abiertas en los indicadores

- KPI-1: cómo se agregan los repuestos y qué es «el método elegido» ([detalle](indicadores/KPI-1-mejora-mae-pronostico.md#ambigüedades)).
- KPI-2: qué es un «componente» y si una publicación del INE cuenta como respaldo ([detalle](indicadores/KPI-2-costo-con-respaldo.md#ambigüedades)).
- KPI-3: qué conjunto es «los datos de movimientos»; con `ventas_simuladas` el valor sería 10 días y cumpliría ([detalle](indicadores/KPI-3-vigencia-datos.md#ambigüedades)).
