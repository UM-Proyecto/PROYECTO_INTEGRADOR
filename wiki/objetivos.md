---
tipo: mapa
fuentes: [F01, F02, F03, F04, F05, F06]
fecha_datos: 2026-10-09
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: borrador
actualizado: 2026-11-03
---

# Objetivos, indicadores y decisión

## Objetivo general

[OBSERVADO] «Determinar las técnicas de análisis de datos que permiten apoyar las decisiones de compra de la empresa MULTIPARTE durante el segundo semestre del 2026» ([F01](../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), «Objetivo general enfocado»; sobre «MULTIPARTE» ver C-01 en el [índice](index.md#contradicciones)).

**Decisión que apoya la wiki:** qué repuesto pedir a China, en qué cantidad y cuándo. **Usuario:** el jefe de compras de MULTIPARTES. F01 no los nombra; la wiki los toma de las instrucciones del proyecto ([AGENTS.md](../AGENTS.md)) [SUPUESTO sobre el usuario, sin fuente en `fuentes/`].

[INFERENCIA] El objetivo general se divide en tres objetivos, uno por cada cosa que una decisión de compra necesita saber y uno por cada criterio aprobado en la HU-33 ([F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md)).

## Mapa

| Objetivo | Qué responde de la decisión | Fuentes | Clase de datos | Indicador | Meta [ESPERADO] | Valor al 3-nov-2026 | Página |
|---|---|---|---|---|---|---|---|
| O1. Cuánto se va a vender | **Cantidad**: cuántas unidades pedir | [F04](fuentes/F04-pronosticos-hu07.md), [F03](fuentes/F03-criterios-exito-hu33.md), [F02](fuentes/F02-registro-fuentes-hu02.md) | FICTICIO | [KPI-1](indicadores/KPI-1-mejora-mae-pronostico.md): mejora del MAE frente a «último periodo» | ≥ 15 % con 1 año + 3 meses reservados | No medible: sin método elegible [OBSERVADO] | [O-1](sintesis/O-1-cuanto-se-vendera.md) |
| O2. Cuánto cuesta traerlo | **Qué** repuesto conviene y por qué medio, según su costo puesto en Santa Cruz | [F05](fuentes/F05-costos-importacion-hu31.md), [F03](fuentes/F03-criterios-exito-hu33.md), [F02](fuentes/F02-registro-fuentes-hu02.md) | MIXTO (valores PUBLICOS) | [KPI-2](indicadores/KPI-2-costo-con-respaldo.md): % de componentes del costo con documento | ≥ 80 % | 40 % (6 de 15) [CALCULADO] | [O-2](sintesis/O-2-cuanto-cuesta-traerlo.md) |
| O3. Con datos al día | **Cuándo**: si los datos con que se decide son recientes | [F02](fuentes/F02-registro-fuentes-hu02.md), [F03](fuentes/F03-criterios-exito-hu33.md) | FICTICIO | [KPI-3](indicadores/KPI-3-vigencia-datos.md): días entre el corte de movimientos y la decisión | ≤ 30 días | 50 días [CALCULADO] | [O-3](sintesis/O-3-datos-al-dia.md) |

Las metas salen de [F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal. Los valores y sus comandos están en cada página de indicador.

## Lectura conjunta

- [INFERENCIA] Al 3-nov-2026 ninguno de los tres criterios alcanza su meta. Uno no se puede medir (O1) y dos se miden y no cumplen (O2 y O3).
- [INFERENCIA] Lo que tienen en común es el insumo que falta: datos propios de MULTIPARTES. O1 necesita historial real de salidas, O2 facturas de importación de la empresa y O3 movimientos con corte reciente.
- [INFERENCIA] Ninguno de los valores calculados sobre datos FICTICIOS describe a la empresa. Sirven para mostrar que los indicadores se pueden calcular y qué les falta.
