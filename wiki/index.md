---
tipo: mapa
subtipo: indice
fuentes: [F01, F02, F03, F04, F05, F06]
fecha: 2026-09-14
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: observado
revision: borrador
actualizado: 2026-11-03
tags: [mapa, ficticio, publico, mixto, moc]
---

# Wiki del proyecto BI de MULTIPARTES

Wiki de conocimiento para apoyar la decisión de compra de MULTIPARTES: qué repuesto pedir a China, en qué cantidad y cuándo. Las reglas para mantenerla están en [[AGENTS]]; las fuentes, en [`fuentes/MANIFIESTO.md`](../fuentes/MANIFIESTO.md).

Clases de datos (nombres del registro de la HU-02): FICTICIO (datos de prueba del equipo, a partir de una muestra inicial de unos 20 registros que facilitó MULTIPARTES), PUBLICO y MIXTO. Un número calculado sobre datos FICTICIOS prueba un método; no describe a la empresa.

## Páginas

### Generales

- [[objetivos]]: mapa objetivo, fuente, indicador, página y decisión, con el valor de cada indicador al 3-nov-2026.
- [[log]]: registro cronológico de las etapas.

### Fuentes

- [[F01-pregunta-enfocada|F01. Pregunta enfocada y objetivo]]: pregunta y objetivo general del proyecto (docx, 14-oct-2026). Sin datos.
- [[F02-registro-fuentes-hu02|F02. Registro de fuentes y fechas (HU-02)]]: diccionario de los 17 conjuntos con clase y fecha de corte. FICTICIO, PUBLICO y MIXTO.
- [[F03-criterios-exito-hu33|F03. Criterios de éxito (HU-33)]]: definición, meta y línea base de los tres indicadores, aprobados el 27-oct-2026.
- [[F04-pronosticos-hu07|F04. Comparación de pronósticos (HU-07)]]: MAE de tres métodos en 10 repuestos, 10 al 14-sep-2026. FICTICIO.
- [[F05-costos-importacion-hu31|F05. Costos de importación (HU-31)]]: 15 componentes del costo con su respaldo, corte 2026-10-09. MIXTO y PUBLICO.
- [[F06-portada-repositorio|F06. Portada del repositorio]]: resumen del equipo sobre origen de datos, historias y criterios (commit `c27757a`).

### Indicadores

- [[KPI-1-mejora-mae-pronostico|KPI-1. Mejora del MAE frente a «último periodo»]]: meta ≥ 15 %; no medible al 3-nov-2026. FICTICIO.
- [[KPI-2-costo-con-respaldo|KPI-2. Componentes del costo con respaldo]]: meta ≥ 80 %; 40 % al 3-nov-2026. MIXTO.
- [[KPI-3-vigencia-datos|KPI-3. Días entre el corte de movimientos y la decisión]]: meta ≤ 30 días; 50 días al 3-nov-2026. FICTICIO.

### Síntesis por objetivo

- [[O-1-cuanto-se-vendera|O1. Cuánto se va a vender]]: pronóstico de salidas; sin técnica recomendable todavía.
- [[O-2-cuanto-cuesta-traerlo|O2. Cuánto cuesta traerlo]]: costo de importación; flete principal con referencias públicas, faltan los costos de llegada y nacionalización.
- [[O-3-datos-al-dia|O3. Con datos al día]]: vigencia de los datos; el registro existe, el corte de movimientos está atrasado.

### Consultas

- [[Q-01-criterios-hu33-al-3-nov|Q-01. Qué criterios de la HU-33 respaldan hoy una decisión de compra]]: respuesta a la pregunta de negocio al 3-nov-2026; ninguno de los tres criterios la respalda todavía. FICTICIO, PUBLICO y MIXTO.

### Revisiones

- [[R-01-salud-3-nov|R-01. Revisión de salud al 3-nov-2026]]: 13 hallazgos que `salud.py` no detecta. Diez quedaron corregidos y tres pendientes: C-05, el aviso vencido de Q-01 y la convención del campo `fecha`. Antigüedad de cada corte de datos. FICTICIO, PUBLICO y MIXTO.

## Contradicciones

| Código | Entre | Qué no coincide | Resolución | Página |
|---|---|---|---|---|
| C-01 | F01 y F06 | El objetivo de F01 dice «MULTIPARTE»; la pregunta de F01 y F06 dicen «MULTIPARTES» ([F01](../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), [F06](../fuentes/F06_portada_repositorio/README.md)) | Prevalece «MULTIPARTES»; parece errata | [[F01-pregunta-enfocada#Contradicciones|F01]] |
| C-02 | F03 y F04 | Historial para el pronóstico: un año + 3 meses reservados ([F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1) frente a 12 meses + 12 meses ([F04](../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo) | Para medir KPI-1 prevalece F03 (criterio aprobado, posterior). **Pendiente** que el equipo alinee la regla de selección | [[KPI-1-mejora-mae-pronostico#Contradicciones|KPI-1]] |
| C-03 | F02 y F06 | HU-32: MIXTO en F06; su conjunto `tc_series_diaria` es PUBLICO en F02 ([F06](../fuentes/F06_portada_repositorio/README.md), fila HU-32; [F02](../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `tc_series_diaria`) | Prevalece F02 para la clase del conjunto. **Pendiente** si falta registrar la parte FICTICIA | [[F02-registro-fuentes-hu02#Contradicciones|F02]] |
| C-04 | F02 y F06 | F06 dice que la HU-31 es MIXTO por «cotizaciones de proveedor FICTICIAS»; la tabla de costos no trae ninguna ([F06](../fuentes/F06_portada_repositorio/README.md), fila HU-31; [F02](../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `costos_importacion` y `cotizaciones_proveedor`) | **Resuelta (revisión 01):** F06 describe la historia, que tiene tres conjuntos en F02 (corregido en R-01; decía dos); las cotizaciones FICTICIAS son otro conjunto. El motivo dado para el MIXTO se discute en C-05 | [[F05-costos-importacion-hu31#Contradicciones|F05]] |
| C-05 | Manifiesto y F06 frente a F02 y F05 | MIXTO es «tablas que combinan datos públicos con datos de prueba» ([manifiesto](../fuentes/MANIFIESTO.md), «Cómo se clasifican los datos»; [F06](../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»), pero la tabla de costos registrada como MIXTO ([F02](../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`) no trae datos de prueba ([F05](../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`) | Para la clase prevalece F02 (MIXTO). **Pendiente** que el equipo diga si debe ser PUBLICO o por qué es MIXTO. No cambia el valor de KPI-2 | [[F05-costos-importacion-hu31#Contradicciones|F05]] |

## Ambigüedades abiertas en los indicadores

- KPI-1: cómo se agregan los repuestos y qué es «el método elegido». Además, ningún repuesto cumple la regla de F04 de tres días con ventas en entrenamiento ([[KPI-1-mejora-mae-pronostico#Ambigüedades|detalle]]).
- KPI-2: qué es un «componente», si una publicación del INE cuenta como respaldo y si importa la antigüedad del documento ([[KPI-2-costo-con-respaldo#Ambigüedades|detalle]]).
- KPI-3: qué conjunto es «los datos de movimientos»; con `ventas_simuladas` el valor sería 10 días y cumpliría. F06 lo resume como «la fecha de los datos», sin más ([[KPI-3-vigencia-datos#Ambigüedades|detalle]]).
