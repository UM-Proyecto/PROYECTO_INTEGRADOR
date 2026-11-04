---
tipo: hallazgo
subtipo: sintesis
fuentes: [F01, F03, F04, F02, F06]
fecha: 2026-09-14
clase_datos: [FICTICIO]
estado: inferido
revision: borrador
actualizado: 2026-11-03
tags: [hallazgo, ficticio]
---

# O1. Cuánto se va a vender

**Pregunta para la decisión de compra:** cuántas unidades de cada repuesto conviene pedir a China, según cuánto se espera vender. **Indicador:** [[KPI-1-mejora-mae-pronostico|KPI-1]]. **Fuentes:** [[F04-pronosticos-hu07|F04]], [[F03-criterios-exito-hu33|F03]], [[F02-registro-fuentes-hu02|F02]].

> Todo el material de este objetivo es FICTICIO: datos de prueba del equipo a partir de una muestra inicial de unos 20 registros que facilitó MULTIPARTES ([F06](../../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»).

## Qué se sabe

- [OBSERVADO] El equipo comparó tres técnicas de pronóstico (último periodo, promedio móvil de 3 días, mismo día de la semana anterior) en 10 repuestos con 14 días de movimientos de septiembre ([F04](../../fuentes/F04_pronosticos_HU07/README.md), párrafos cuarto y sexto).
- [CALCULADO] El MAE medio sobre esos datos FICTICIOS es 0,14, 0,14 y 0,32 unidades por día; ninguna técnica mejora a la referencia ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `mae`; cálculo en [[KPI-1-mejora-mae-pronostico|KPI-1]]).
- [OBSERVADO] Ninguna de las 30 combinaciones repuesto-método queda seleccionada; todas dicen SIN_SELECCION_FIABLE ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `seleccion`).

## Qué significa para la decisión

- [INFERENCIA] Hoy la wiki **no puede recomendar** una técnica de pronóstico para decidir cantidades. El procedimiento de comparación existe y corre; lo que falta es historial.
- [INFERENCIA] Mientras no haya un método elegido, cualquier cantidad que se pida sale del criterio del jefe de compras, no de un pronóstico validado.
- [INFERENCIA] Con 7 de 10 repuestos sin ventas en la ventana evaluada, el problema no es sólo el largo del historial: muchos repuestos tienen ventas esporádicas, y un MAE bajo no distingue un buen pronóstico de un repuesto que no se vende. Esto es una lectura de datos FICTICIOS y habrá que comprobarla con datos reales.

## Qué falta

1. Historial de al menos un año con 3 meses reservados ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1).
2. [OBSERVADO] El resultado de la HU-36 con 284 días, que no está en `fuentes/` ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-36).
3. Una decisión del equipo sobre C-02 (un año + 3 meses en F03 frente a 12 + 12 meses en F04). Ver [[KPI-1-mejora-mae-pronostico#Contradicciones|KPI-1]].
4. Datos de faltantes de stock, para no confundir ventas observadas con demanda ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo).

**Estado del objetivo:** [INFERENCIA] no medible al 3-nov-2026.
