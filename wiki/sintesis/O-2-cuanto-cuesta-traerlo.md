---
tipo: sintesis
fuentes: [F03, F05, F02, F06]
fecha_datos: 2026-10-09
clase_datos: [MIXTO, PUBLICO]
estado: borrador
actualizado: 2026-11-03
---

# O2. Cuánto cuesta traerlo

**Pregunta para la decisión de compra:** cuánto cuesta poner un repuesto de China en Santa Cruz, para saber si conviene pedirlo y por qué medio. **Indicador:** [KPI-2](../indicadores/KPI-2-costo-con-respaldo.md). **Fuentes:** [F05](../fuentes/F05-costos-importacion-hu31.md), [F03](../fuentes/F03-criterios-exito-hu33.md), [F02](../fuentes/F02-registro-fuentes-hu02.md).

> La tabla de costos es MIXTO según F02 y sus valores vienen de fuentes PUBLICAS (agente de carga, SCFI, INE). No son la tarifa que pagaría MULTIPARTES. Ver C-04 en [F05](../fuentes/F05-costos-importacion-hu31.md#contradicciones).

## Qué se sabe

- [OBSERVADO] Hay referencias públicas del flete principal desde China: cotizaciones indicativas de un agente de carga de 2026-06 para contenedor de 20 pies (4797 a 5870 USD), de 40 pies (5327 a 6532 USD), LCL (93 USD por m³), aéreo (11 USD por kg) y express (18,76 USD por kg) ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `valor_min`, `valor_max` y `unidad`). Clase: PUBLICO.
- [OBSERVADO] Hay estimaciones del flete y seguro implícitos (CIF − FOB) por medio, sacadas del INE para 2025-09 a 2026-08; por ejemplo, 0,1673 USD por kg por carretera (7,8 % del FOB) y 3,2056 USD por kg por vía aérea (11,5 % del FOB) ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `valor_min` y `unidad`). Son agregados de aduana, no tarifas.
- [CALCULADO] 6 de 15 componentes tienen respaldo documentado: 40 %, frente a una meta de 80 % ([KPI-2](../indicadores/KPI-2-costo-con-respaldo.md)).
- [OBSERVADO] No hay ningún dato de seguro separado, nacionalización y agente aduanero, comisiones de gestión ni flete terrestre de Arica o Iquique a Santa Cruz ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), filas PENDIENTE).

## Qué significa para la decisión

- [INFERENCIA] Con lo que hay se puede comparar **órdenes de magnitud** del flete principal entre medios (contenedor, consolidado, aéreo), pero no calcular el costo puesto en Santa Cruz: faltan los cuatro componentes de llegada y nacionalización, que son los que paga directamente MULTIPARTES.
- [INFERENCIA] El costo de importación es hoy el objetivo más cercano a la información real del mercado (fuentes públicas), pero el más lejano a los costos propios de la empresa.

## Qué falta

1. Facturas o cotizaciones de MULTIPARTES para los 4 componentes PENDIENTE ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `nota`).
2. Al menos 2 documentos más para pasar de 10 a 12 de 15 (ver cálculo en [KPI-2](../indicadores/KPI-2-costo-con-respaldo.md#qué-falta)).
3. Que el equipo aclare qué cuenta como «componente» y resuelva C-04.
4. El archivo del INE con su URL de descarga, para poder recalcular las 5 estimaciones (manifiesto, fila F05).

**Estado del objetivo:** no cumple al 3-nov-2026 (40 % frente a 80 %).
