---
tipo: hallazgo
subtipo: sintesis
fuentes: [F01, F03, F04, F02, F06, F07]
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
- [CALCULADO] El MAE medio sobre esos datos FICTICIOS es 0,14, 0,14 y 0,32 unidades por día; ninguna técnica mejora a la referencia, y en los 3 repuestos con ventas las tres empatan en 0,467 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `mae`; cálculo en [[KPI-1-mejora-mae-pronostico|KPI-1]]).
- [OBSERVADO] Ninguna de las 30 combinaciones repuesto-método queda seleccionada; todas dicen SIN_SELECCION_FIABLE ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `seleccion`).

## Qué significa para la decisión

- [INFERENCIA] Hoy la wiki **no puede recomendar** una técnica de pronóstico para decidir cantidades. El procedimiento de comparación existe y corre. Desde la segunda ingesta, lo que falta ya no es historial de prueba: [[F07-datos-simulados-hu34|F07]] trae uno. Falta correr la comparación sobre él y acordar la regla de selección (C-02).
- [INFERENCIA] Mientras no haya un método elegido, cualquier cantidad que se pida sale del criterio del jefe de compras, no de un pronóstico validado.
- [INFERENCIA] Con 7 de 10 repuestos sin ventas en la ventana evaluada, el problema no es sólo el largo del historial: muchos repuestos tienen ventas esporádicas, y un MAE bajo no distingue un buen pronóstico de un repuesto que no se vende. Esto es una lectura de datos FICTICIOS y habrá que comprobarla con datos reales.
- [CALCULADO] La otra simulación del equipo no repite ese patrón. En las ventas FICTICIAS de la HU-34 sólo el 9,0 % de los días repuesto tienen cero ventas, y cada uno de los 30 repuestos vende entre 504 y 657 de los 662 días ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `unidades_vendidas`; comando en [[F07-datos-simulados-hu34#Cómo recalcular|F07]]). [INFERENCIA] Las dos simulaciones describen repuestos muy distintos, así que ninguna de las dos dice cómo se venden los repuestos de MULTIPARTES; sólo el historial real lo dirá.

## Qué falta

1. [OBSERVADO] Historial de al menos un año con 3 meses reservados ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). [CALCULADO] Como dato FICTICIO ya existe: las ventas de la HU-34 cubren 662 días ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `fecha`; detalle en [[KPI-1-mejora-mae-pronostico#Qué falta|KPI-1]]). Falta la comparación de métodos sobre ese historial y, para hablar de la empresa, el historial real.
2. [OBSERVADO] El resultado de la HU-36 con 284 días, que no está en `fuentes/` ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-36).
3. [OBSERVADO] Una decisión del equipo sobre C-02 (un año + 3 meses en F03 frente a 12 + 12 meses en F04). Ver [[KPI-1-mejora-mae-pronostico#Contradicciones|KPI-1]].
4. [INFERENCIA] Datos de faltantes de stock, para no confundir ventas observadas con demanda ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo).
5. [INFERENCIA] Repuestos con ventas suficientes en entrenamiento. F04 pide tres días con ventas y ninguno de los 10 repuestos FICTICIOS los tiene: cada uno tiene uno o ninguno ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `dias_con_ventas_entrenamiento`; detalle en [[KPI-1-mejora-mae-pronostico#Valor al 3-nov-2026|KPI-1]]). Un historial más largo no alcanza si los repuestos casi no se venden.

**Estado del objetivo:** [INFERENCIA] no medible al 3-nov-2026.

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]] (H-05 y H-08): se agregó el ítem 5 y se etiquetaron los ítems 1, 3 y 4. La conclusión no cambia.
- 2026-11-03, segunda ingesta ([[F07-datos-simulados-hu34|F07]]): decía «lo que falta es historial». Ahora dice que el historial de prueba existe y que falta la comparación sobre él y la regla de selección. Se agregó el contraste con las ventas de F07 y la nota al ítem 1. El estado sigue en «no medible».
