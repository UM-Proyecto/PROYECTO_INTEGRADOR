---
tipo: indicador
subtipo: indicador
fuentes: [F03, F02, F06, F07]
fecha: 2026-09-14
clase_datos: [FICTICIO]
estado: esperado
revision: borrador
actualizado: 2026-11-03
tags: [indicador, ficticio]
---

# KPI-3. Días entre el corte de los movimientos y la decisión de compra

**Objetivo:** [[O-3-datos-al-dia|O3, con datos al día]]. **Criterio:** HU-33, criterio 3 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3).

> Las fechas de corte que usa este indicador son de conjuntos FICTICIOS. El cálculo prueba cómo se medirá la vigencia; no dice cuán al día están los datos reales de MULTIPARTES.

## Definición

| Campo | Valor |
|---|---|
| Fórmula | Días = fecha de la decisión de compra − fecha hasta la que llegan los datos de movimientos ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3, columna Indicador) [OBSERVADO] |
| Unidad | Días calendario ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3, columna Unidad; que sean calendario y no hábiles es [SUPUESTO], porque 42 días entre 14-sep y 26-oct sólo da en días calendario) |
| Granularidad | Una medición por decisión de compra (por fecha de decisión) |
| Período | Puntual: se mide en la fecha de cada decisión. Línea base al 26-oct-2026; valor recalculado al 3-nov-2026 |
| Filtros | Conjuntos de movimientos del registro: `movimientos_inventario` y `historial_movimientos` (los dos llegan al 2026-09-14) ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`). Ver ambigüedad 1 |
| Fuente | Registro de fuentes y fechas (HU-02): [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv). Clase de los conjuntos: FICTICIO |
| Meta | [ESPERADO] 30 días o menos ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3) |
| Línea base | [OBSERVADO] 42 días (movimientos al 14-sep, medido el 26-oct-2026) ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3). [CALCULADO] 2026-10-26 − 2026-09-14 = 42 días: coincide |

## Valor al 3-nov-2026

- [SUPUESTO] Se toma como fecha de decisión el 3-nov-2026, que es la fecha de la pregunta de negocio de la wiki. No hay una decisión de compra fechada en las fuentes.
- [CALCULADO] 2026-11-03 − 2026-09-14 = **50 días** ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas `movimientos_inventario` e `historial_movimientos`, columna `fecha_corte_datos`).
- [CALCULADO] **Estado frente a la meta: no cumple** (50 días frente a 30; [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `movimientos_inventario`, y [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3). Como el corte no se movió, el valor sube un día por cada día que pasa; ya superaba la meta en la línea base.
- [CALCULADO] Para cumplir la meta al 3-nov-2026, los movimientos tendrían que llegar al menos al 2026-10-04 (3-nov menos los 30 días de la meta de [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3).

## Ambigüedades

1. **Qué conjunto es «los datos de movimientos».** F03 usa los movimientos al 14-sep. F02 registra además `ventas_simuladas` e `inventario_simulado` al 2026-10-24 y `compras_simuladas` al 2026-10-23, también FICTICIOS ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas de la HU-34). [OBSERVADO] F06 lo deja todavía más abierto: resume el criterio como «Días entre la fecha de los datos y la decisión de compra», sin decir «de movimientos» ([F06](../../fuentes/F06_portada_repositorio/README.md), «Criterios de éxito (HU-33)»). Prevalece F03 porque F06 es un resumen.

   **Lo que agrega F07 (segunda ingesta, 3-nov-2026).** [OBSERVADO] La descripción de la HU-34 muestra que dos de sus conjuntos son movimientos en sentido estricto: el inventario diario trae `entradas` y `salidas` por repuesto, las salidas igualan a las ventas y las entradas a las compras recibidas ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: inventario» y «Construcción y verificación»). Con eso hay cinco fechas posibles, todas FICTICIAS:

   | Conjunto candidato | Hasta dónde llega | Días al 3-nov-2026 [CALCULADO] | ¿Cumple ≤ 30? |
   |---|---|---|---|
   | `movimientos_inventario` e `historial_movimientos` (HU-17 y HU-30; los que usa F03) | 2026-09-14 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`) | 50 | No |
   | Ventas diarias de la HU-34 | 2026-10-24, leído en el propio archivo ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `fecha`) | 10 | Sí, hasta el 2026-11-23 |
   | Inventario diario de la HU-34 (entradas y salidas) | 2026-10-24 ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: inventario») | 10 | Sí, hasta el 2026-11-23 |
   | Compras de la HU-34, por fecha de recepción | 2026-10-23 ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: compras») | 11 | Sí, hasta el 2026-11-22 |
   | Compras de la HU-34, por fecha de pedido | 2026-09-24 (misma sección) | 40 | No |

   [INFERENCIA] F07 no resuelve la ambigüedad: no menciona la HU-33 ni el criterio 3, y F03 nombra como fuente el registro de la HU-02, en el que los conjuntos de la HU-34 ya estaban cargados el 27-oct. Lo que sí hace es acotarla: si el equipo acepta los datos de la HU-34 como «movimientos», el indicador pasa de 50 a 10 días y cumple la meta, pero sólo por tres semanas sin carga nueva, y mide la vigencia de una simulación que la propia fuente dice que no representa a la empresa ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Naturaleza y alcance»). La wiki sigue a F03 (movimientos de la HU-17 y la HU-30) porque es la definición aprobada. Queda **pendiente** que el equipo fije el conjunto; la tabla de arriba es lo que necesita para decidirlo.
2. [INFERENCIA] **Qué es «la fecha de la decisión».** No hay decisiones de compra registradas en las fuentes. Sin ese dato el indicador se mide contra una fecha supuesta.
3. [OBSERVADO] **Fecha de medición de la línea base.** F03 la fecha el 26-oct, pero la única carga del registro F02 es del 27-oct 18:00 UTC ([F02](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv), columna `fecha_intento`). La fecha de corte no cambia, así que el valor de 42 días se sostiene.
4. [INFERENCIA] **Vigencia de los otros insumos.** El indicador mira sólo los movimientos. Los costos (cotizaciones de 2026-06) y el INE (hasta 2026-08) también envejecen y no entran en ningún indicador ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`). La antigüedad de cada conjunto al 3-nov-2026 está en [[R-01-salud-3-nov#H-09. Antigüedad de cada corte al 3-nov-2026|R-01]].

## Cómo recalcular

    python3 -c "import csv,datetime as d;r={x['conjunto']:x['fecha_corte_datos'] for x in csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8'))};h=d.date(2026,11,3);print({k:(h-d.date.fromisoformat(r[k])).days for k in ['movimientos_inventario','historial_movimientos','ventas_simuladas']})"

Última fecha de las ventas FICTICIAS de F07, leída en el propio CSV, días al 3-nov-2026 y último día en que cumpliría la meta:

    python3 -c "import csv,datetime as d;r=list(csv.DictReader(open('fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv',encoding='utf-8-sig')));m=d.date.fromisoformat(max(x['fecha'] for x in r));print(m,(d.date(2026,11,3)-m).days,m+d.timedelta(days=30))"

## Cambios

- [CALCULADO] 2026-11-03, segunda ingesta ([[F07-datos-simulados-hu34|F07]]): la ambigüedad 1 ahora compara los cinco candidatos con su fecha y su valor, y se agregó el comando que lee la fecha en el CSV de ventas. Antes la wiki conocía las fechas de la HU-34 sólo por el registro F02; ahora la de ventas está verificada en el archivo. El valor (50 días), el estado frente a la meta (no cumple) y el pendiente no cambian.

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: se agregó a la ambigüedad 1 la redacción de F06 (H-06) y se etiquetaron las ambigüedades 2 y 4 (H-08). El valor y el estado frente a la meta no cambian.
