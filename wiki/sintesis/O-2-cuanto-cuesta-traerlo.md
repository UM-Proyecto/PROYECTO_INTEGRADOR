---
tipo: hallazgo
subtipo: sintesis
fuentes: [F03, F05, F02, F06]
fecha: 2026-10-09
clase_datos: [MIXTO, PUBLICO]
estado: inferido
revision: borrador
actualizado: 2026-11-03
tags: [hallazgo, mixto, publico]
---

# O2. Cuánto cuesta traerlo

**Pregunta para la decisión de compra:** cuánto cuesta poner un repuesto de China en Santa Cruz, para saber si conviene pedirlo y por qué medio. **Indicador:** [[KPI-2-costo-con-respaldo|KPI-2]]. **Fuentes:** [[F05-costos-importacion-hu31|F05]], [[F03-criterios-exito-hu33|F03]], [[F02-registro-fuentes-hu02|F02]].

> La tabla de costos es MIXTO según F02 y sus valores vienen de fuentes PUBLICAS (agente de carga, SCFI, INE). No son la tarifa que pagaría MULTIPARTES. Ver C-04 y C-05 en [[F05-costos-importacion-hu31#Contradicciones|F05]].

## Qué se sabe

- [OBSERVADO] Hay referencias públicas del flete principal desde China: cotizaciones indicativas de un agente de carga de 2026-06 para contenedor de 20 pies (4797 a 5870 USD), de 40 pies (5327 a 6532 USD), LCL (93 USD por m³), aéreo (11 USD por kg) y express (18,76 USD por kg) ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `valor_min`, `valor_max` y `unidad`). Clase: PUBLICO.
- [OBSERVADO] Hay estimaciones del flete y seguro implícitos (CIF − FOB) por medio, sacadas del INE para 2025-09 a 2026-08; por ejemplo, 0,1673 USD por kg por carretera (7,8 % del FOB) y 3,2056 USD por kg por vía aérea (11,5 % del FOB) ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `valor_min` y `unidad`). Son agregados de aduana, no tarifas.
- [CALCULADO] 6 de 15 componentes tienen respaldo documentado: 40 %, frente a una meta de 80 % ([[KPI-2-costo-con-respaldo|KPI-2]]).
- [OBSERVADO] La tabla de costos no trae ningún valor de seguro separado, nacionalización y agente aduanero, comisiones de gestión ni flete terrestre de Arica o Iquique a Santa Cruz ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), filas PENDIENTE).
- [OBSERVADO] F02 registra aparte un conjunto FICTICIO, `costos_complementarios`, descrito como «Seguro y otros costos de importación», con 4 registros y corte 2026-09 ([F02](../../fuentes/F02_registro_fuentes_HU02/conjuntos.csv), fila `costos_complementarios`). Su archivo no está en `fuentes/`. [INFERENCIA] Puede que sean valores de prueba para los mismos cuatro componentes; aunque lo fueran, un valor FICTICIO no es un documento de respaldo y no mejora KPI-2.

## Qué significa para la decisión

- [INFERENCIA] Con lo que hay se puede comparar **órdenes de magnitud** del flete principal entre medios (contenedor, consolidado, aéreo), pero no calcular el costo puesto en Santa Cruz: faltan los cuatro componentes de llegada y nacionalización, que son los que paga directamente MULTIPARTES.
- [INFERENCIA] El costo de importación es hoy el objetivo más cercano a la información real del mercado (fuentes públicas), pero el más lejano a los costos propios de la empresa.

## Qué falta

1. [OBSERVADO] Facturas o cotizaciones de MULTIPARTES para los 4 componentes PENDIENTE ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`).
2. [CALCULADO] Al menos 2 documentos más para pasar de 10 a 12 de 15 (ver cálculo en [[KPI-2-costo-con-respaldo#Qué falta|KPI-2]]).
3. [INFERENCIA] Que el equipo aclare qué cuenta como «componente», porque las cinco cotizaciones son alternativas de transporte y no partes que se suman (ambigüedad 1 de [[KPI-2-costo-con-respaldo#Ambigüedades|KPI-2]]).
4. [OBSERVADO] El archivo del INE con su URL de descarga, para poder recalcular las 5 estimaciones ([manifiesto](../../fuentes/MANIFIESTO.md), fila F05).
5. [INFERENCIA] Que el equipo resuelva C-05: por qué la tabla de costos es MIXTO si no trae datos de prueba ([[F05-costos-importacion-hu31#Contradicciones|F05]]). No cambia el 40 %; cambia cómo se describe la clase de los datos de este objetivo.

**Estado del objetivo:** [CALCULADO] no cumple al 3-nov-2026 (40 % frente a 80 %; ver [[KPI-2-costo-con-respaldo|KPI-2]]).

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: «no hay ningún dato» pasó a «la tabla de costos no trae ningún valor», con la mención de `costos_complementarios` (H-04). El ítem 3 remitía a C-04, que no trata de qué es un componente, y ahora remite a la ambigüedad de KPI-2. Se agregó el ítem 5 sobre C-05 (H-02) y se etiquetaron los ítems 1, 3 y 4 (H-08).
