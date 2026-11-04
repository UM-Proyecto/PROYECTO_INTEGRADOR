---
tipo: decision
subtipo: mapa
fuentes: [F01, F02, F03, F04, F05, F06]
fecha: 2026-10-09
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: esperado
revision: borrador
actualizado: 2026-11-03
tags: [decision, ficticio, publico, mixto]
---

# Objetivos, indicadores y decisión

## Objetivo general

[OBSERVADO] «Determinar las técnicas de análisis de datos que permiten apoyar las decisiones de compra de la empresa MULTIPARTE durante el segundo semestre del 2026» ([F01](../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), «Objetivo general enfocado»; sobre «MULTIPARTE» ver C-01 en el [[index#Contradicciones|índice]]).

**Decisión que apoya la wiki:** qué repuesto pedir a China, en qué cantidad y cuándo. **Usuario:** el jefe de compras de MULTIPARTES. F01 no los nombra; la wiki los toma de las instrucciones del proyecto ([[AGENTS]]) [SUPUESTO sobre el usuario, sin fuente en `fuentes/`].

[INFERENCIA] El objetivo general se divide en tres objetivos, uno por cada cosa que una decisión de compra necesita saber y uno por cada criterio aprobado en la HU-33 ([F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md)).

## Mapa

| Objetivo | Qué responde de la decisión | Fuentes | Clase de datos | Indicador | Meta [ESPERADO] | Valor al 3-nov-2026 | Página |
|---|---|---|---|---|---|---|---|
| O1. Cuánto se va a vender | **Cantidad**: cuántas unidades pedir | [[F04-pronosticos-hu07|F04]], [[F03-criterios-exito-hu33|F03]], [[F02-registro-fuentes-hu02|F02]] | FICTICIO | [[KPI-1-mejora-mae-pronostico|KPI-1]]: mejora del MAE frente a «último periodo» | ≥ 15 % con 1 año + 3 meses reservados | No medible: sin método elegible [INFERENCIA] | [[O-1-cuanto-se-vendera|O-1]] |
| O2. Cuánto cuesta traerlo | **Qué** repuesto conviene y por qué medio, según su costo puesto en Santa Cruz | [[F05-costos-importacion-hu31|F05]], [[F03-criterios-exito-hu33|F03]], [[F02-registro-fuentes-hu02|F02]] | MIXTO (valores PUBLICOS) | [[KPI-2-costo-con-respaldo|KPI-2]]: % de componentes del costo con documento | ≥ 80 % | 40 % (6 de 15) [CALCULADO] | [[O-2-cuanto-cuesta-traerlo|O-2]] |
| O3. Con datos al día | **Cuándo**: si los datos con que se decide son recientes | [[F02-registro-fuentes-hu02|F02]], [[F03-criterios-exito-hu33|F03]] | FICTICIO | [[KPI-3-vigencia-datos|KPI-3]]: días entre el corte de movimientos y la decisión | ≤ 30 días | 50 días [CALCULADO] | [[O-3-datos-al-dia|O-3]] |

Las metas salen de [F03](../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal. Los valores y sus comandos están en cada página de indicador.

## Lectura conjunta

- [INFERENCIA] Al 3-nov-2026 ninguno de los tres criterios alcanza su meta. Uno no se puede medir (O1) y dos se miden y no cumplen (O2 y O3).
- [INFERENCIA] Lo que tienen en común es el insumo que falta: datos propios de MULTIPARTES. O1 necesita historial real de salidas, O2 facturas de importación de la empresa y O3 movimientos con corte reciente.
- [INFERENCIA] Ninguno de los valores calculados sobre datos FICTICIOS describe a la empresa. Sirven para mostrar que los indicadores se pueden calcular y qué les falta.
- [INFERENCIA] La respuesta a la pregunta de negocio, con lo que la evidencia sostiene y lo que no, está en [[Q-01-criterios-hu33-al-3-nov|la consulta Q-01]]. La revisión de salud del 3-nov-2026 está en [[R-01-salud-3-nov|R-01]].

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]] (H-07): el «No medible» de O1 pasó de [OBSERVADO] a [INFERENCIA], porque es una conclusión, igual que en [[KPI-1-mejora-mae-pronostico|KPI-1]].
