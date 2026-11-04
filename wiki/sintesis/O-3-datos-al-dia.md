---
tipo: hallazgo
subtipo: sintesis
fuentes: [F03, F02, F05]
fecha: 2026-09-14
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: inferido
revision: borrador
actualizado: 2026-11-03
tags: [hallazgo, ficticio, publico, mixto]
---

# O3. Con datos al día

**Pregunta para la decisión de compra:** si los datos con los que se decide cuándo pedir reflejan lo que pasa hoy en el inventario. **Indicador:** [[KPI-3-vigencia-datos|KPI-3]]. **Fuentes:** [[F02-registro-fuentes-hu02|F02]], [[F03-criterios-exito-hu33|F03]].

> Los conjuntos de movimientos que mide el indicador son FICTICIOS. El registro F02 también incluye conjuntos PUBLICOS y uno MIXTO, cuyas fechas se citan abajo como contexto.

## Qué se sabe

- [OBSERVADO] El registro de la HU-02 guarda, para 17 conjuntos, la fecha hasta la que llegan sus datos; las 17 cargas del 27-oct-2026 salieron bien ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columnas `fecha_corte_datos` y `estado_ultima_carga`).
- [CALCULADO] Los movimientos FICTICIOS llegan al 14-sep-2026: al 3-nov-2026 son 50 días, frente a una meta de 30 ([[KPI-3-vigencia-datos|KPI-3]]).
- [OBSERVADO] Otros insumos tienen cortes distintos: tipo de cambio PUBLICO al 2026-10-26, referencias de flete PUBLICAS al 2026-10-09, INE PUBLICO al 2026-08, tabla de costos MIXTO al 2026-10-09 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`).

## Qué significa para la decisión

- [INFERENCIA] El mecanismo para medir la vigencia ya existe: el registro guarda la fecha de corte de cada conjunto y avisa si una carga falla. Lo que no existe es un flujo de datos que lo mantenga al día.
- [INFERENCIA] Con el conjunto que define F03, la meta no se cumple y empeora con cada día que pasa sin carga nueva. Con los datos simulados de la HU-34 (al 24-oct), el valor sería de 10 días y la cumpliría. Mientras el equipo no fije el conjunto, el estado del objetivo depende de una elección de definición, no de los datos (ambigüedad 1 de [[KPI-3-vigencia-datos#Ambigüedades|KPI-3]]).
- [INFERENCIA] Al ser datos FICTICIOS, el valor mide la vigencia de los datos de prueba del equipo, no la de los sistemas de MULTIPARTES.

## Qué falta

1. [INFERENCIA] Que el equipo nombre el conjunto exacto que cuenta como «datos de movimientos» (ambigüedad 1 de [[KPI-3-vigencia-datos#Ambigüedades|KPI-3]]).
2. [CALCULADO] Una carga de movimientos con corte el 2026-10-04 o después, para cumplir la meta al 3-nov-2026: 2026-11-03 − 2026-10-04 = 30 días ([[KPI-3-vigencia-datos|KPI-3]]).
3. Una fecha de decisión de compra registrada; hoy se usa la fecha de la consulta como [SUPUESTO].

[CALCULADO] El indicador mira sólo los movimientos, pero el corte de un conjunto puede esconder filas más viejas: `flete_referencias` figura al 2026-10-09 por el índice SCFI, y las 5 cotizaciones del agente de carga que respaldan KPI-2 son de 2026-06, 154 días al 3-nov-2026 ([F05](../../fuentes/F05_costos_importacion_HU31/flete_referencias_puntuales.csv), columna `fecha_dato`). La antigüedad de cada conjunto está en [[R-01-salud-3-nov#H-09. Antigüedad de cada corte al 3-nov-2026|R-01]].

**Estado del objetivo:** [CALCULADO] no cumple al 3-nov-2026 con la definición de F03 (50 días frente a 30; ver [[KPI-3-vigencia-datos|KPI-3]]).

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]] (H-01): decía «corte posterior al 2026-10-04». Un corte el mismo 2026-10-04 ya cumple la meta, como dice KPI-3. Se agregó también la nota sobre la antigüedad de las cotizaciones (H-09).
