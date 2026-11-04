---
tipo: indicador
subtipo: indicador
fuentes: [F03, F05, F02]
fecha: 2026-10-09
clase_datos: [MIXTO, PUBLICO]
estado: esperado
revision: borrador
actualizado: 2026-11-03
tags: [indicador, mixto, publico]
---

# KPI-2. Porcentaje de componentes del costo de importación con respaldo

**Objetivo:** [[O-2-cuanto-cuesta-traerlo|O2, cuánto cuesta traerlo]]. **Criterio:** HU-33, criterio 2 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2).

> La tabla de costos es MIXTO según F02; sus valores vienen de referencias PUBLICAS (agente de carga, SCFI, INE) y de filas sin dato; no trae datos FICTICIOS. Ver C-04, resuelta, y C-05, pendiente: con la definición de MIXTO del manifiesto, una tabla sin datos de prueba no sería MIXTO ([[F05-costos-importacion-hu31#Contradicciones|F05]]).

## Definición

| Campo | Valor |
|---|---|
| Fórmula | % = componentes con respaldo DOCUMENTADO / total de componentes × 100 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2, columna Indicador; respaldo = valor de la columna `tipo_dato` de [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv)) [OBSERVADO] |
| Unidad | % de componentes ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2, columna Unidad) |
| Granularidad | Componente del costo (una fila de la tabla de costos) |
| Período | Foto a la fecha de corte de la tabla: 2026-10-09 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`, columna `fecha_corte_datos`). Las filas tienen fechas propias: 2026-06, 2026-10-09 y 2025-09 a 2026-08 ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `fecha_dato`) |
| Filtros | Ninguno: cuentan las 15 filas de la tabla |
| Fuente | Costos de importación (HU-31): [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv). Clase MIXTO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`) |
| Meta | [ESPERADO] 80 % o más ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2) |
| Línea base | [OBSERVADO] 6 de 15 documentados (40 %), medida el 26-oct-2026 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2); desglose: 5 estimados y 4 pendientes ([F03](../../fuentes/F03_criterios_exito_HU33/BORRADOR_criterios_exito.md), criterio 3) |

## Valor al 3-nov-2026

- [CALCULADO] 6 DOCUMENTADO, 5 ESTIMACION y 4 PENDIENTE sobre 15 filas: 6 / 15 × 100 = **40 %** ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`). Igual a la línea base: la tabla no cambió entre el 26-oct y el 3-nov (misma huella en [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `sha256`, y en `fuentes/MANIFIESTO.csv`).
- [CALCULADO] Para llegar al 80 % hacen falta 12 de 15 documentados (0,8 × 15 = 12, sobre las 15 filas de [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv)), es decir **6 componentes más**.
- [CALCULADO] **Estado frente a la meta: no cumple** (40 % frente a 80 %; [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv) y [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 2).

## Qué falta

- [OBSERVADO] Los 4 PENDIENTE (seguro separado, nacionalización y agente aduanero, comisiones de gestión, flete terrestre a Santa Cruz) piden «facturas al encargado de compras» ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`).
- [CALCULADO] Aunque se documenten los 4 pendientes, el indicador llegaría a 10 / 15 = 66,7 % ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`). [INFERENCIA] Para pasar el 80 % también hay que convertir al menos 2 de las 5 ESTIMACION del INE en un documento (por ejemplo, una factura de flete real de MULTIPARTES por ese medio).
- [OBSERVADO] F02 registra un conjunto FICTICIO, `costos_complementarios` («Seguro y otros costos de importación», 4 registros, corte 2026-09), que no está en `fuentes/` ([F02](../../fuentes/F02_registro_fuentes_HU02/conjuntos.csv), fila `costos_complementarios`). [INFERENCIA] Aunque tuviera valores para los 4 PENDIENTE, un dato FICTICIO no es un documento de respaldo y no cuenta para este indicador.

## Ambigüedades

1. **Qué es un «componente».** Las 5 cotizaciones DOCUMENTADO del agente de carga son **alternativas** (FCL 20, FCL 40, LCL, aéreo, express), no partes que se suman; un pedido usa una sola. El índice SCFI es un índice de mercado en puntos, no un costo en dólares ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `concepto` y `unidad`). Si se contaran componentes de un pedido real (flete principal, seguro, nacionalización, comisiones, flete terrestre), el denominador y el numerador cambiarían. La wiki sigue el conteo de F03 por filas y anota la duda [INFERENCIA].
2. [INFERENCIA] **Qué cuenta como respaldo.** F03 acepta «factura, cotización o publicación». Las 5 ESTIMACION salen de una publicación del INE pero se marcan ESTIMACION porque son un agregado declarado en aduana y no una tarifa ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`). Con la letra de F03 se podrían contar; con la clasificación de F05, no. La línea base de F03 (40 %) sigue a F05.
3. [INFERENCIA] **Vigencia del respaldo.** El indicador no pide que el documento esté al día. Las cotizaciones son de 2026-06 ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `fecha_dato`) y la meta del 80 % se podría cumplir con documentos viejos. [CALCULADO] Al 3-nov-2026, 5 de los 6 respaldos DOCUMENTADO tienen 154 días (página del agente de carga modificada el 2026-06-02, columna `nota`), aunque el registro fecha el conjunto de referencias al 2026-10-09 por el índice SCFI ([[R-01-salud-3-nov#H-09. Antigüedad de cada corte al 3-nov-2026|R-01]], H-09).
4. [INFERENCIA] **Del mercado o de la empresa.** Las cotizaciones son indicativas, no la tarifa de MULTIPARTES ([manifiesto](../../fuentes/MANIFIESTO.md), fila F05). El indicador no distingue entre respaldo de mercado y respaldo propio de la empresa.

## Cómo recalcular

    python3 -c "import csv;k=list(csv.DictReader(open('fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv',encoding='utf-8')));d=sum(x['tipo_dato']=='DOCUMENTADO' for x in k);print(d,len(k),round(d/len(k)*100,1))"

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: el 66,7 % pasó de [INFERENCIA] a [CALCULADO] (H-07). Se agregaron la mención de `costos_complementarios` (H-04), la antigüedad de los respaldos (H-09) y el aviso de C-05 (H-02). El valor (40 %) y el estado (no cumple) no cambian.
