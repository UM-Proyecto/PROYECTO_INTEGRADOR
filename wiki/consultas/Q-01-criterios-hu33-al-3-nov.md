---
tipo: hallazgo
subtipo: consulta
fuentes: [F02, F03, F04, F05, F06]
fecha: 2026-09-14
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: inferido
revision: revisado
actualizado: 2026-11-03
tags: [hallazgo, consulta, ficticio, publico, mixto]
---

# Q-01. Qué criterios de la HU-33 respaldan hoy una decisión de compra

**Pregunta de negocio:** «Con la evidencia disponible al 3 de noviembre de 2026, ¿cuáles de los tres criterios de éxito de la HU-33 pueden respaldar hoy una decisión de compra de MULTIPARTES, qué valor tiene cada uno frente a su meta y qué falta para los que no la alcanzan?» (instrucciones del proyecto, [[AGENTS]]).

**Páginas leídas:** [[index]], [[objetivos]], [[KPI-1-mejora-mae-pronostico|KPI-1]], [[KPI-2-costo-con-respaldo|KPI-2]], [[KPI-3-vigencia-datos|KPI-3]], [[O-1-cuanto-se-vendera|O-1]], [[O-2-cuanto-cuesta-traerlo|O-2]], [[O-3-datos-al-dia|O-3]] y las páginas de fuentes que citan. Las cifras se volvieron a calcular desde `fuentes/` el 3-nov-2026 con los comandos de la sección «Cómo recalcular».

> Esta respuesta afecta una decisión de compra. La revisó el equipo el 3-nov-2026 (revisión 02, sección «Verificación»; aviso actualizado en la revisión 03). Dos de los tres criterios se miden sobre datos FICTICIOS (datos de prueba del equipo, ampliados desde una muestra inicial de unos 20 registros que facilitó MULTIPARTES); sus valores prueban el método y no describen a la empresa.

## Respuesta corta

[INFERENCIA] **Ninguno de los tres criterios puede respaldar hoy una decisión de compra de MULTIPARTES.** KPI-1 no se puede medir, y KPI-2 y KPI-3 se miden pero no alcanzan su meta. Además, KPI-1 y KPI-3 descansan en datos FICTICIOS, así que aunque cumplieran no dirían nada de la empresa; KPI-2 es el único que usa valores PUBLICOS reales, y es justamente el que queda más lejos de los costos propios de MULTIPARTES (ver [[O-2-cuanto-cuesta-traerlo|O-2]]).

## Valor de cada criterio frente a su meta

Metas y líneas base de [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal; valores recalculados en cada página de indicador.

| Criterio | Meta | Línea base (26-oct-2026) | Valor al 3-nov-2026 | Estado | Clase de los datos | ¿Respalda la decisión hoy? |
|---|---|---|---|---|---|---|
| [[KPI-1-mejora-mae-pronostico|KPI-1]]. Mejora del MAE frente a «último periodo» | [ESPERADO] ≥ 15 % con un año de historial y 3 meses reservados | [OBSERVADO] «Sin método elegible» | [CALCULADO] Sin método elegido; como prueba del cálculo, 0 % (promedio móvil) y −128,6 % (mismo día de la semana) sobre una ventana de 5 días ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `metodo` y `mae`). En los 3 repuestos con ventas los tres métodos empatan (ver «Verificación») | No medible | FICTICIO | No |
| [[KPI-2-costo-con-respaldo|KPI-2]]. Componentes del costo con respaldo | [ESPERADO] ≥ 80 % | [OBSERVADO] 6 de 15 (40 %) | [CALCULADO] 6 / 15 = 40 % ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`) | No cumple: faltan 6 componentes | MIXTO según F02, con el motivo en discusión (C-05); los 6 documentados son valores PUBLICOS y las 5 estimaciones son cálculos sobre datos PUBLICOS del INE | No |
| [[KPI-3-vigencia-datos|KPI-3]]. Días entre el corte de movimientos y la decisión | [ESPERADO] ≤ 30 días | [OBSERVADO] 42 días | [CALCULADO] 2026-11-03 − 2026-09-14 = 50 días ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `movimientos_inventario`, columna `fecha_corte_datos`) | No cumple: 20 días de más | FICTICIO | No |

## Lo que la evidencia sostiene

- [OBSERVADO] Las 30 combinaciones repuesto-método de la HU-07 dicen SIN_SELECCION_FIABLE; no hay método elegido contra el cual medir KPI-1 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `seleccion`).
- [CALCULADO] En 7 de los 10 repuestos FICTICIOS no hubo ventas en la ventana de evaluación, así que la referencia da MAE 0 y la mejora queda indefinida para ellos ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `dias_con_ventas_evaluacion`, filas `ultimo_periodo`).
- [CALCULADO] La tabla de costos tiene 6 componentes DOCUMENTADO, 5 ESTIMACION y 4 PENDIENTE ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato`). El valor de KPI-2 no cambió desde la línea base del 26-oct.
- [OBSERVADO] Lo documentado son referencias públicas del flete principal: cinco cotizaciones indicativas de un agente de carga de 2026-06 y el índice SCFI ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `concepto` y `fecha_dato`). No son la tarifa de MULTIPARTES ([manifiesto](../../fuentes/MANIFIESTO.md), fila F05).
- [OBSERVADO] Los conjuntos de movimientos `movimientos_inventario` e `historial_movimientos`, ambos FICTICIOS, llegan al 2026-09-14 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columnas `tipo_dato` y `fecha_corte_datos`).
- [INFERENCIA] Los tres indicadores se pueden calcular con un comando desde `fuentes/`. El mecanismo de medición existe para los tres; lo que falta son los insumos.

## Lo que la evidencia no sostiene

- [INFERENCIA] Que alguna técnica de pronóstico sea mejor o peor que «último periodo». El 0 % de mejora del promedio móvil sale de 5 días de datos FICTICIOS y no es un resultado sobre la demanda de MULTIPARTES.
- [CALCULADO] Que «mismo día de la semana» sea peor. Su −128,6 % sale entero de REP-0001 y REP-0003, dos repuestos sin ventas en la evaluación en los que pronosticó ventas (MAE 1,0 y 0,8); en los 3 repuestos con ventas los tres métodos dan el mismo MAE, 0,467 unidades por día ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `codigo_unico`, `metodo`, `mae` y `dias_con_ventas_evaluacion`). Corregido en la revisión 02.
- [INFERENCIA] Un costo puesto en Santa Cruz. Con lo que hay se comparan órdenes de magnitud del flete principal entre medios, pero faltan los cuatro componentes de llegada y nacionalización ([[O-2-cuanto-cuesta-traerlo|O-2]]).
- [INFERENCIA] Que los datos de MULTIPARTES estén atrasados. Los 50 días de KPI-3 miden la vigencia de datos de prueba del equipo, no la de los sistemas de la empresa.
- [CALCULADO] Que KPI-3 «cumpla». Con el conjunto `ventas_simuladas` (FICTICIO, corte 2026-10-24) el valor sería 10 días y cumpliría ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `ventas_simuladas`), pero F03 define el indicador con los movimientos al 14-sep; usar el otro conjunto sería cambiar la definición sin acuerdo del equipo (ambigüedad 1 de [[KPI-3-vigencia-datos#Ambigüedades|KPI-3]]).

## Qué falta para cada criterio

| Criterio | Insumo que falta | Cuánto falta |
|---|---|---|
| KPI-1 | [OBSERVADO] Historial de salidas de al menos un año más 3 meses reservados, idealmente el historial real de MULTIPARTES ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1); una regla de selección acordada (C-02) | [CALCULADO] Hoy la evaluación cubre 5 días (2026-09-10 a 2026-09-14, [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `desde_evaluacion` y `hasta_evaluacion`). La repetición de la HU-36 con 284 días no está en `fuentes/` ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-36) y, aun así, 284 días son menos que los 365 + 3 meses que pide F03 |
| KPI-2 | [OBSERVADO] Facturas o cotizaciones de MULTIPARTES para seguro separado, nacionalización y agente aduanero, comisiones de gestión y flete terrestre a Santa Cruz ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), filas PENDIENTE, columna `nota`) | [CALCULADO] 6 documentos más para llegar a 12 de 15 (0,8 × 15). Con sólo los 4 pendientes se llega a 10 / 15 = 66,7 %; hacen falta además 2 de las 5 ESTIMACION convertidas en documento ([[KPI-2-costo-con-respaldo#Qué falta|KPI-2]]) |
| KPI-3 | [OBSERVADO] Una carga de movimientos con corte reciente y una fecha de decisión de compra registrada ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3) | [CALCULADO] Para cumplir al 3-nov-2026 el corte debe llegar al menos al 2026-10-04 (3-nov − 30 días); el actual está 20 días antes de esa fecha ([[KPI-3-vigencia-datos|KPI-3]]) |

[INFERENCIA] El insumo común a los tres es el mismo: datos propios de MULTIPARTES (historial de salidas, facturas de importación y movimientos al día). Con ellos las líneas base se vuelven a medir, como ya prevé F03 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), párrafo inicial).

## Vacíos e incertidumbres

1. [SUPUESTO] La fecha de decisión de KPI-3 es el 3-nov-2026, la fecha de esta consulta; no hay ninguna decisión de compra fechada en las fuentes.
2. [SUPUESTO] KPI-1 se agrega como promedio simple del MAE entre repuestos; F03 no fija cómo se agregan ([[KPI-1-mejora-mae-pronostico#Ambigüedades|KPI-1]]).
3. [INFERENCIA] KPI-2 cuenta filas de la tabla, pero las 5 cotizaciones documentadas son alternativas de transporte, no partes que se suman. Si se contaran los componentes de un pedido real, el porcentaje cambiaría ([[KPI-2-costo-con-respaldo#Ambigüedades|KPI-2]]).
4. [INFERENCIA] F03 acepta «publicación» como respaldo; si las 5 estimaciones del INE se contaran como documentadas, KPI-2 subiría a 11 / 15 = 73,3 % y seguiría sin cumplir. La línea base de F03 no las cuenta.
5. [OBSERVADO] C-02 sigue pendiente: F03 pide un año más 3 meses reservados y F04 exige 12 meses más 12 meses para seleccionar un método ([[KPI-1-mejora-mae-pronostico#Contradicciones|KPI-1]]).
6. [OBSERVADO] El archivo del INE con su URL de descarga no está en `fuentes/`, así que las 5 estimaciones no se pueden recalcular desde su origen ([manifiesto](../../fuentes/MANIFIESTO.md), fila F05).

## Verificación (revisión 02)

Tres afirmaciones de esta respuesta se contrastaron con los archivos originales de `fuentes/` y con cálculos reproducibles en `src/u4-t1/verificar.py` (códigos Q1 a Q3; la salida queda en `data/processed/u4-t1/verificaciones.csv`). Las notas de la revisión están en `docs/u4-t1/evidencia/revisiones/02.md`.

| Código | Afirmación de la respuesta | Contra qué | Resultado |
|---|---|---|---|
| Q1 y Q1b | KPI-1: mejora de 0 % (promedio móvil) y −128,6 % (mismo día de la semana) | [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), MAE por repuesto y método | [CALCULADO] Las cifras coinciden, pero la lectura estaba incompleta: en los 3 repuestos con ventas los métodos empatan (0,467) y el −128,6 % sale de 2 repuestos sin ventas. Se corrigió la tabla y se agregó la afirmación a «Lo que la evidencia no sostiene» |
| Q2 | KPI-3: el corte tendría que llegar al 2026-10-04 y el actual está 20 días antes | [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `movimientos_inventario`; meta de [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md) | [CALCULADO] Coincide |
| Q3 | KPI-2: 66,7 % con los 4 pendientes, 73,3 % contando las estimaciones, meta de 12 de 15 | [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna `tipo_dato` | [CALCULADO] Coincide. Se precisó que las 5 estimaciones no son valores publicados sino cálculos sobre datos del INE |

## Cómo recalcular

Desde la raíz del repositorio. KPI-1 (MAE medio y mejora por método, y conteo de `seleccion`):

    python3 -c "import csv,collections;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));m=collections.defaultdict(list);[m[x['metodo']].append(float(x['mae'])) for x in f];b=sum(m['ultimo_periodo'])/len(m['ultimo_periodo']);print({k:(round(sum(v)/len(v),3),round((b-sum(v)/len(v))/b*100,1)) for k,v in m.items()},collections.Counter(x['seleccion'] for x in f))"

KPI-2 (conteo por respaldo):

    python3 -c "import csv,collections;print(collections.Counter(x['tipo_dato'] for x in csv.DictReader(open('fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv',encoding='utf-8'))))"

KPI-3 (días al 3-nov-2026 por conjunto):

    python3 -c "import csv,datetime as d;r={x['conjunto']:x['fecha_corte_datos'] for x in csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8'))};h=d.date(2026,11,3);print({k:(h-d.date.fromisoformat(r[k])).days for k in ['movimientos_inventario','historial_movimientos','ventas_simuladas']})"
