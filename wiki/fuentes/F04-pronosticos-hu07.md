---
tipo: fuente
subtipo: fuente
fuentes: [F04, F02, F06]
fecha: 2026-09-14
clase_datos: [FICTICIO]
estado: observado
revision: borrador
actualizado: 2026-11-03
tags: [fuente, ficticio]
---

# F04. Comparación de pronósticos (HU-07)

**Archivos:** [`comparacion_pronosticos.csv`](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv) y [`README.md`](../../fuentes/F04_pronosticos_HU07/README.md). **Historia:** HU-07, SCRUM-20, Fiorella Sandoval. **Clase:** FICTICIO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `comparacion_pronosticos`). **Ventana evaluada:** 10 al 14 de septiembre de 2026.

> Todo lo de esta página está calculado sobre datos FICTICIOS. Los MAE prueban que el procedimiento funciona; no dicen nada sobre la demanda real de MULTIPARTES.

## Qué dice

- [OBSERVADO] Se comparan tres métodos: último periodo, promedio móvil de tres días y mismo día de la semana anterior. Se reservan los últimos cinco días y se calcula MAE en unidades por día sobre las mismas fechas para cada repuesto ([F04](../../fuentes/F04_pronosticos_HU07/README.md), cuarto párrafo).
- [OBSERVADO] La entrada son las salidas `ORIGINAL` del reporte de depuración de la HU-17; los días sin salidas cuentan como cero ventas observadas, «que pueden ser menores que la demanda real si hubo faltantes de stock» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), tercer párrafo).
- [OBSERVADO] Para seleccionar un método se exigen al menos 12 meses de entrenamiento, 12 meses reservados, tres días con ventas en entrenamiento, ventas en cada mes evaluado y ninguna salida pendiente de revisión ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo).
- [OBSERVADO] «El archivo actual contiene movimientos del 1 al 14 de septiembre de 2026. Por eso sus MAE son una comprobación técnica del procedimiento y ninguna selección sirve todavía como base confiable para compras» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), sexto párrafo).

## Cifras

| Cálculo | Valor | Etiqueta |
|---|---|---|
| Filas del CSV | 30 (10 repuestos × 3 métodos) | [CALCULADO] |
| Filas con `seleccion` = SIN_SELECCION_FIABLE | 30 de 30 | [CALCULADO] |
| Periodos evaluados por repuesto | 5 (2026-09-10 a 2026-09-14) | [OBSERVADO], columnas `periodos_evaluados`, `desde_evaluacion`, `hasta_evaluacion` |
| Repuestos sin ventas en la ventana evaluada | 7 de 10 | [CALCULADO], columna `dias_con_ventas_evaluacion` = 0 |
| MAE medio, último periodo | 0,14 unidades/día (suma 1,4 / 10) | [CALCULADO] |
| MAE medio, promedio móvil de 3 días | 0,14 unidades/día (suma 1,4 / 10) | [CALCULADO] |
| MAE medio, mismo día de la semana | 0,32 unidades/día (suma 3,2 / 10) | [CALCULADO] |

Fuente de todas las filas: [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `metodo`, `mae`, `seleccion` y `dias_con_ventas_evaluacion`. El MAE medio entre repuestos es un agregado que hace la wiki; F04 no lo publica. Ese promedio mezcla repuestos con y sin ventas en la evaluación: en los 3 con ventas los tres métodos empatan en 0,467 (ver [[Q-01-criterios-hu33-al-3-nov#Verificación (revisión 02)|Q-01]]).

- [INFERENCIA] Con 7 de 10 repuestos sin ventas en evaluación, un MAE de cero no valida ningún método; el propio CSV lo dice en la columna `limitaciones` («sin ventas registradas en evaluacion: MAE cero no valida el metodo»).

## Vacíos

- [OBSERVADO] La repetición con 284 días de historial (HU-36, SCRUM-47) figura como «Pendiente de subir» y «Resultado comentado en Jira» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla de historias, fila HU-36). No está en `fuentes/`, así que la wiki no puede usar su resultado.
- [OBSERVADO] El README remite a `reports/hu-07/REPORTE_HU07.md`, que no fue copiado a `fuentes/` ([F04](../../fuentes/F04_pronosticos_HU07/README.md), primer párrafo).

## Contradicciones

- **C-02.** El historial que pide F04 para seleccionar (12 + 12 meses) no coincide con el que pide F03 para el criterio 1 (un año + 3 meses). Ver [[KPI-1-mejora-mae-pronostico#Contradicciones|KPI-1]].

## Cómo recalcular

    python3 -c "import csv,collections;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));m=collections.defaultdict(list);[m[x['metodo']].append(float(x['mae'])) for x in f];print({k:(round(sum(v),3),len(v),round(sum(v)/len(v),3)) for k,v in m.items()});print(collections.Counter(x['seleccion'] for x in f));print(sum(1 for x in f if x['metodo']=='ultimo_periodo' and x['dias_con_ventas_evaluacion']=='0'))"
