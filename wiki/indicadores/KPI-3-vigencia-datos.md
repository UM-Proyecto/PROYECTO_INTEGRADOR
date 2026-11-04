---
tipo: indicador
fuentes: [F03, F02]
fecha_datos: 2026-09-14
clase_datos: [FICTICIO]
estado: borrador
actualizado: 2026-11-03
---

# KPI-3. Días entre el corte de los movimientos y la decisión de compra

**Objetivo:** [O3, con datos al día](../sintesis/O-3-datos-al-dia.md). **Criterio:** HU-33, criterio 3 ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3).

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
- [CALCULADO] **Estado frente a la meta: no cumple** (50 días frente a 30). Como el corte no se movió, el valor sube un día por cada día que pasa; ya superaba la meta en la línea base.
- [CALCULADO] Para cumplir la meta al 3-nov-2026, los movimientos tendrían que llegar al menos al 2026-10-04 (3-nov menos los 30 días de la meta de [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3).

## Ambigüedades

1. **Qué conjunto es «los datos de movimientos».** F03 usa los movimientos al 14-sep. F02 registra además `ventas_simuladas` e `inventario_simulado` al 2026-10-24 y `compras_simuladas` al 2026-10-23, también FICTICIOS ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), filas de la HU-34). [CALCULADO] Con `ventas_simuladas`, el valor sería 2026-11-03 − 2026-10-24 = 10 días y **cumpliría** la meta. El resultado depende del conjunto elegido, y F03 no lo nombra por su identificador. La wiki sigue a F03 (movimientos de la HU-17 y la HU-30) porque es la definición aprobada; queda **pendiente** que el equipo fije el conjunto.
2. **Qué es «la fecha de la decisión».** No hay decisiones de compra registradas en las fuentes. Sin ese dato el indicador se mide contra una fecha supuesta.
3. [OBSERVADO] **Fecha de medición de la línea base.** F03 la fecha el 26-oct, pero la única carga del registro F02 es del 27-oct 18:00 UTC ([F02](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv), columna `fecha_intento`). La fecha de corte no cambia, así que el valor de 42 días se sostiene.
4. **Vigencia de los otros insumos.** El indicador mira sólo los movimientos. Los costos (cotizaciones de 2026-06) y el INE (hasta 2026-08) también envejecen y no entran en ningún indicador ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`).

## Cómo recalcular

    python3 -c "import csv,datetime as d;r={x['conjunto']:x['fecha_corte_datos'] for x in csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8'))};h=d.date(2026,11,3);print({k:(h-d.date.fromisoformat(r[k])).days for k in ['movimientos_inventario','historial_movimientos','ventas_simuladas']})"
