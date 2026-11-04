---
tipo: fuente
fuentes: [F03, F04, F06]
fecha_datos: 2026-10-26
clase_datos: [FICTICIO, MIXTO]
estado: revisado
actualizado: 2026-11-03
---

# F03. Criterios de éxito (HU-33)

**Archivos:** [`CRITERIOS_APROBADOS.md`](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md) (los tres criterios aprobados) y [`BORRADOR_criterios_exito.md`](../../fuentes/F03_criterios_exito_HU33/BORRADOR_criterios_exito.md) (cinco candidatos con su detalle). **Historia:** HU-33, SCRUM-44, Samuel Castillo. **Aprobación:** 27-oct-2026. **Líneas base:** medidas el 26-oct-2026.

F03 es la **definición de los indicadores** de la wiki. Cuando el aprobado y el borrador difieren, prevalece el aprobado; el borrador sirve para el detalle que el aprobado resume.

## Qué dice

- [OBSERVADO] El equipo aprobó tres criterios el 27 de octubre de 2026 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), primer párrafo).
- [OBSERVADO] «Las líneas base se midieron con los datos FICTICIOS del repositorio al 26 de octubre de 2026 y se vuelven a medir cuando lleguen los datos de MULTIPARTES» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), primer párrafo).
- [OBSERVADO] Quedaron fuera, como referencia, «inventario registrado igual al físico (HU-18)» y «horas para preparar un pedido» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), último párrafo).

| # | Criterio | Meta [ESPERADO] | Línea base al 26-oct-2026 [OBSERVADO] | Página |
|---|---|---|---|---|
| 1 | Pronóstico de salidas mejor que «último periodo» (MAE) | ≥ 15 % menos de error, con un año de historial y 3 meses reservados | Sin método elegible: HU-07 sólo cubre del 1 al 14 de septiembre | [KPI-1](../indicadores/KPI-1-mejora-mae-pronostico.md) |
| 2 | Costo de importación con respaldo | ≥ 80 % de componentes documentados | 6 de 15 documentados (40 %) | [KPI-2](../indicadores/KPI-2-costo-con-respaldo.md) |
| 3 | Datos vigentes al decidir | ≤ 30 días | 42 días (movimientos al 14-sep, medido el 26-oct) | [KPI-3](../indicadores/KPI-3-vigencia-datos.md) |

Fuente de la tabla: [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal.

## Lo que aporta el borrador

- [OBSERVADO] Las metas «son una propuesta para discutir» y las líneas base salen de datos FICTICIOS ([F03](../../fuentes/F03_criterios_exito_HU33/BORRADOR_criterios_exito.md), primer párrafo). El manifiesto agrega que las metas las propuso el equipo y no salen de una norma.
- [OBSERVADO] El criterio 2 aprobado viene con el desglose de la línea base: «6 de 15 componentes documentados (40 %), 5 estimados y 4 pendientes» ([F03](../../fuentes/F03_criterios_exito_HU33/BORRADOR_criterios_exito.md), criterio 3 del borrador).
- [OBSERVADO] El criterio descartado de inventario tenía línea base «9 de 13 conteos sin diferencia (69 %)» y el de horas por pedido no se midió en MULTIPARTES ([F03](../../fuentes/F03_criterios_exito_HU33/BORRADOR_criterios_exito.md), criterios 2 y 5). La wiki no los sigue.

## Contradicciones

- **C-02. Historial necesario para el criterio 1.** [OBSERVADO] F03 pide «un año de historial y 3 meses reservados» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1, columna Meta). La herramienta de la HU-07 exige, para seleccionar un método, «al menos 12 meses de entrenamiento, 12 meses reservados para evaluación» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo). Detalle y resolución en [KPI-1](../indicadores/KPI-1-mejora-mae-pronostico.md#contradicciones).
- [INFERENCIA] El criterio 3 se fecha el 26-oct, pero la carga del registro que cita como fuente (F02) es del 27-oct 18:00 UTC ([F02](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv), columna `fecha_intento`). No cambia el valor porque la fecha de corte de los movimientos (14-sep) es la misma, pero la medición no se puede reproducir con el archivo de F02 tal como está. Se anota como ambigüedad, no como contradicción.
