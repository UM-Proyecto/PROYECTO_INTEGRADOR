---
tipo: indicador
subtipo: indicador
fuentes: [F03, F04, F02]
fecha: 2026-09-14
clase_datos: [FICTICIO]
estado: esperado
revision: borrador
actualizado: 2026-11-03
tags: [indicador, ficticio]
---

# KPI-1. Mejora del MAE del pronóstico frente a «último periodo»

**Objetivo:** [[O-1-cuanto-se-vendera|O1, cuánto se va a vender]]. **Criterio:** HU-33, criterio 1 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1).

> Los valores de esta página salen de datos FICTICIOS. Prueban el método de cálculo; no describen la demanda de MULTIPARTES.

## Definición

| Campo | Valor |
|---|---|
| Fórmula | Mejora (%) = (MAE_ref − MAE_elegido) / MAE_ref × 100, donde MAE_ref es el del método «último periodo» y MAE_elegido el del método elegido, ambos sobre el mismo periodo reservado. MAE = promedio de \|venta observada − pronóstico\| por día ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1, columna Indicador; [F04](../../fuentes/F04_pronosticos_HU07/README.md), cuarto párrafo) [OBSERVADO para el MAE; la forma de la fórmula de mejora es INFERENCIA a partir de «% de mejora sobre la referencia»] |
| Unidad | MAE en unidades de repuesto por día; mejora en % ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1, columna Unidad) |
| Granularidad | Repuesto (`codigo_unico`) × día ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo) |
| Período | Entrenamiento de un año y 3 meses reservados para evaluación ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1, columna Meta). En la línea base: evaluación del 2026-09-10 al 2026-09-14 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `desde_evaluacion` y `hasta_evaluacion`) |
| Filtros | Sólo salidas `ORIGINAL`; se excluyen duplicados y salidas pendientes de revisión; días sin salidas = 0 ventas observadas ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo) |
| Fuente | Historial de movimientos (HU-30) y comparación de pronósticos (HU-07): [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv); registro en [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `historial_movimientos` y `comparacion_pronosticos`. Clase: FICTICIO |
| Meta | [ESPERADO] Al menos 15 % menos de error que «último periodo», con un año de historial y 3 meses reservados ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1) |
| Línea base | [OBSERVADO] «Sin método elegible: HU-07 solo cubre del 1 al 14 de septiembre», medida el 26-oct-2026 sobre datos FICTICIOS ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1, columna Línea base) |

## Valor al 3-nov-2026

- [CALCULADO] Sobre los 10 repuestos FICTICIOS de F04, el MAE medio es 0,14 unidades/día para «último periodo», 0,14 para promedio móvil de 3 días y 0,32 para mismo día de la semana. La mejora frente a la referencia es 0 % para el promedio móvil y −128,6 % para mismo día de la semana: (0,14 − 0,32) / 0,14 × 100 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `metodo` y `mae`). Comando abajo. [CALCULADO] Corrección de la revisión 02: en los 3 repuestos con ventas en la evaluación los tres métodos dan el mismo MAE, 0,467 unidades por día; la diferencia del promedio sale de REP-0001 y REP-0003, sin ventas en la evaluación, donde «mismo día de la semana» pronosticó ventas (MAE 1,0 y 0,8) ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `dias_con_ventas_evaluacion`; ver [[Q-01-criterios-hu33-al-3-nov#Verificación (revisión 02)|Q-01]]).
- [OBSERVADO] Las 30 filas tienen `seleccion` = SIN_SELECCION_FIABLE ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `seleccion`).
- [CALCULADO] Las 30 filas también traen en `limitaciones` el texto «menos de 3 dias con ventas en entrenamiento». En `dias_con_ventas_entrenamiento`, 8 de los 10 repuestos tienen 0 y 2 (REP-0001 y REP-0003) tienen 1 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `limitaciones` y `dias_con_ventas_entrenamiento`). F04 pide tres para seleccionar ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo). [INFERENCIA] La falta de selección no viene sólo del largo del historial: además hay muy pocas ventas. El empate en 0,467 se explica igual. Los 3 repuestos con ventas en la evaluación no vendieron nada en entrenamiento, así que los tres métodos pronostican cero y el MAE de cada uno es lo que se vendió (revisión de salud [[R-01-salud-3-nov#H-05. Por qué ningún método queda seleccionado|R-01]], H-05).
- [INFERENCIA] El indicador **no se puede medir todavía**: no hay método elegido, la ventana evaluada es de 5 días y no de 3 meses, y 7 de 10 repuestos no tienen ventas en esa ventana. Las cifras de arriba no sirven para decir si la meta se cumple; sólo muestran que el cálculo corre. **Estado frente a la meta: no medible.**

## Qué falta

- [OBSERVADO] Un historial de al menos un año con 3 meses reservados ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). F02 registra un `historial_movimientos` FICTICIO de 1220 registros que llega al 2026-09-14 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `historial_movimientos`), pero F04 no lo usa: su entrada es el reporte de depuración de septiembre ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo).
- [OBSERVADO] El resultado de la HU-36 (284 días de historial) no está en `fuentes/` ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-36).
- [INFERENCIA] Aun si F04 usara `historial_movimientos`, F02 lo describe como un «Historial de doce meses con precios» ([F02](../../fuentes/F02_registro_fuentes_HU02/conjuntos.csv), fila `historial_movimientos`, columna `descripcion`): menos que el año más 3 meses que pide F03.
- [INFERENCIA] Para que el valor diga algo sobre MULTIPARTES hace falta el historial real de salidas de la empresa; con datos FICTICIOS el indicador sólo prueba el método.

## Ambigüedades

1. **Cómo se agregan los repuestos.** F03 no dice si la mejora se mide por repuesto, como promedio de MAE entre repuestos o sobre el total. La wiki usa el promedio simple entre repuestos [SUPUESTO].
2. [OBSERVADO] **Qué es «el método elegido».** F03 no fija la regla de elección. F04 sí tiene una (columna `seleccion`), pero con otro requisito de historial ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo; ver C-02).
3. **Unidad.** F03 dice «repuestos por día» y F04 «unidades por día». La wiki entiende unidades vendidas de cada repuesto por día [INFERENCIA].
4. [OBSERVADO] **Ventas observadas frente a demanda.** Los días sin salidas cuentan como cero aunque haya habido faltante de stock ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo). Un MAE bajo puede venir de stock agotado y no de un buen pronóstico.
5. [CALCULADO] **MAE cero.** Con 7 de 10 repuestos sin ventas en evaluación ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `dias_con_ventas_evaluacion`), la referencia da MAE 0 en esos repuestos y la fórmula de mejora queda indefinida para ellos (división por cero).

## Contradicciones

- **C-02. Historial para elegir un método.** [OBSERVADO] F03: «al menos 15 % menos de error que la referencia, con un año de historial y 3 meses reservados» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). F04: «La selección requiere al menos 12 meses de entrenamiento, 12 meses reservados para evaluación» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo). Con 15 meses de historial se cumpliría F03 y la herramienta de F04 seguiría marcando SIN_SELECCION_FIABLE. **Resolución parcial:** para medir el indicador prevalece F03, porque es el criterio aprobado por el equipo el 27-oct-2026 y es posterior a la HU-07 (evaluada en septiembre). **Pendiente** que el equipo decida si ajusta la regla de selección de la HU-07 o la meta de la HU-33; hasta entonces la wiki no puede afirmar que un método «elegido» por F04 cumpla F03.

## Cómo recalcular

    python3 -c "import csv,collections;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));m=collections.defaultdict(list);[m[x['metodo']].append(float(x['mae'])) for x in f];b=sum(m['ultimo_periodo'])/len(m['ultimo_periodo']);print({k:(round(sum(v)/len(v),3),round((b-sum(v)/len(v))/b*100,1)) for k,v in m.items()})"

Días con ventas en entrenamiento por repuesto y filas con la limitación de menos de tres días:

    python3 -c "import csv;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));print({x['codigo_unico']:x['dias_con_ventas_entrenamiento'] for x in f if x['metodo']=='ultimo_periodo'},sum('menos de 3 dias con ventas en entrenamiento' in x['limitaciones'] for x in f))"

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: se agregó que ningún repuesto cumple la regla de tres días con ventas en entrenamiento y por qué empatan los métodos (H-05), y la nota sobre los doce meses de `historial_movimientos`. Se etiquetaron las ambigüedades 2 y 4 (H-08). El estado frente a la meta sigue siendo «no medible».
