---
tipo: indicador
fuentes: [F03, F04, F02]
fecha_datos: 2026-09-14
clase_datos: [FICTICIO]
estado: borrador
actualizado: 2026-11-03
---

# KPI-1. Mejora del MAE del pronóstico frente a «último periodo»

**Objetivo:** [O1, cuánto se va a vender](../sintesis/O-1-cuanto-se-vendera.md). **Criterio:** HU-33, criterio 1 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1).

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

- [CALCULADO] Sobre los 10 repuestos FICTICIOS de F04, el MAE medio es 0,14 unidades/día para «último periodo», 0,14 para promedio móvil de 3 días y 0,32 para mismo día de la semana. La mejora frente a la referencia es 0 % para el promedio móvil y −128,6 % para mismo día de la semana: (0,14 − 0,32) / 0,14 × 100 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `metodo` y `mae`). Comando abajo.
- [OBSERVADO] Las 30 filas tienen `seleccion` = SIN_SELECCION_FIABLE ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `seleccion`).
- [INFERENCIA] El indicador **no se puede medir todavía**: no hay método elegido, la ventana evaluada es de 5 días y no de 3 meses, y 7 de 10 repuestos no tienen ventas en esa ventana. Las cifras de arriba no sirven para decir si la meta se cumple; sólo muestran que el cálculo corre. **Estado frente a la meta: no medible.**

## Qué falta

- [OBSERVADO] Un historial de al menos un año con 3 meses reservados ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). F02 registra un `historial_movimientos` FICTICIO de 1220 registros que llega al 2026-09-14 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `historial_movimientos`), pero F04 no lo usa: su entrada es el reporte de depuración de septiembre ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo).
- [OBSERVADO] El resultado de la HU-36 (284 días de historial) no está en `fuentes/` ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-36).
- [INFERENCIA] Para que el valor diga algo sobre MULTIPARTES hace falta el historial real de salidas de la empresa; con datos FICTICIOS el indicador sólo prueba el método.

## Ambigüedades

1. **Cómo se agregan los repuestos.** F03 no dice si la mejora se mide por repuesto, como promedio de MAE entre repuestos o sobre el total. La wiki usa el promedio simple entre repuestos [SUPUESTO].
2. **Qué es «el método elegido».** F03 no fija la regla de elección. F04 sí tiene una (columna `seleccion`), pero con otro requisito de historial (ver C-02).
3. **Unidad.** F03 dice «repuestos por día» y F04 «unidades por día». La wiki entiende unidades vendidas de cada repuesto por día [INFERENCIA].
4. **Ventas observadas frente a demanda.** Los días sin salidas cuentan como cero aunque haya habido faltante de stock ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo). Un MAE bajo puede venir de stock agotado y no de un buen pronóstico.
5. **MAE cero.** Con 7 de 10 repuestos sin ventas en evaluación, la referencia da MAE 0 en esos repuestos y la fórmula de mejora queda indefinida para ellos (división por cero).

## Contradicciones

- **C-02. Historial para elegir un método.** [OBSERVADO] F03: «al menos 15 % menos de error que la referencia, con un año de historial y 3 meses reservados» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). F04: «La selección requiere al menos 12 meses de entrenamiento, 12 meses reservados para evaluación» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo). Con 15 meses de historial se cumpliría F03 y la herramienta de F04 seguiría marcando SIN_SELECCION_FIABLE. **Resolución parcial:** para medir el indicador prevalece F03, porque es el criterio aprobado por el equipo el 27-oct-2026 y es posterior a la HU-07 (evaluada en septiembre). **Pendiente** que el equipo decida si ajusta la regla de selección de la HU-07 o la meta de la HU-33; hasta entonces la wiki no puede afirmar que un método «elegido» por F04 cumpla F03.

## Cómo recalcular

    python3 -c "import csv,collections;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));m=collections.defaultdict(list);[m[x['metodo']].append(float(x['mae'])) for x in f];b=sum(m['ultimo_periodo'])/len(m['ultimo_periodo']);print({k:(round(sum(v)/len(v),3),round((b-sum(v)/len(v))/b*100,1)) for k,v in m.items()})"
