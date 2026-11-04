---
tipo: fuente
fuentes: [F02, F06]
fecha_datos: 2026-10-27
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: revisado
actualizado: 2026-11-03
---

# F02. Registro de fuentes y fechas (HU-02)

**Archivos:** [`registro_actualizaciones.csv`](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv) (estado actual, un renglón por conjunto), [`conjuntos.csv`](../../fuentes/F02_registro_fuentes_HU02/conjuntos.csv) (definición de cada conjunto: archivo, fuente, clase, responsable, columnas obligatorias y columna de fecha), [`historial_cargas.csv`](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv) (cada intento de carga) y [`LEEME.md`](../../fuentes/F02_registro_fuentes_HU02/LEEME.md). **Historia:** HU-02, SCRUM-12, Samuel Castillo. **Carga registrada:** 27-oct-2026 18:00 UTC.

F02 hace de **diccionario de datos** de la wiki: dice qué es cada conjunto, de dónde viene, si es FICTICIO, PUBLICO o MIXTO, y hasta qué fecha llegan sus datos. Es un registro de metadatos, no los datos.

## Qué dice

- [OBSERVADO] El registro tiene 17 conjuntos ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), un renglón por conjunto).
- [CALCULADO] Por clase (columna `tipo_dato`): 13 FICTICIO, 3 PUBLICO y 1 MIXTO. Coincide con lo que dice el manifiesto. Comando abajo.
- [CALCULADO] Los 17 conjuntos tienen `estado_ultima_carga` = OK, y `historial_cargas.csv` tiene un solo intento por conjunto, todos del 27-oct-2026 18:00 UTC ([F02](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv), columnas `fecha_intento` y `resultado`).
- [OBSERVADO] Una carga cuenta como fallida si falta el archivo, no se lee como texto, le falta una columna obligatoria, no tiene registros o trae una fecha mal escrita; una fecha vacía no es fallo, y un rango como `2025-09 a 2026-08` cuenta por su fecha final ([F02](../../fuentes/F02_registro_fuentes_HU02/LEEME.md), sección «Cuándo una carga se toma como fallida»).

## Diccionario resumido

Fechas de corte y conteos tomados de [`registro_actualizaciones.csv`](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columnas `conjunto`, `tipo_dato`, `responsable`, `fecha_corte_datos` y `registros` [OBSERVADO]. Los conjuntos que usan los indicadores están marcados.

| Conjunto | Qué es | Clase | Responsable | Corte de datos | Registros | Lo usa |
|---|---|---|---|---|---|---|
| catalogo_repuestos | Catálogo de repuestos | FICTICIO | Sabrina | (sin columna de fecha) | 20 | |
| movimientos_inventario | Movimientos de septiembre | FICTICIO | Sabrina | 2026-09-14 | 24 | [KPI-3](../indicadores/KPI-3-vigencia-datos.md) |
| reporte_depuracion | Movimientos depurados (HU-17) | FICTICIO | Sabrina | 2026-09-14 | 24 | entrada de F04 |
| stock_inicial | Stock inicial por repuesto | FICTICIO | Sabrina | 2026-08-31 | 10 | |
| conteos_fisicos | Conteos físicos | FICTICIO | Sabrina | 2026-09-30 | 13 | |
| historial_ajustes | Ajustes de inventario (HU-18) | FICTICIO | Sabrina | 2026-10-02 10:05:00 | 6 | |
| comparacion_pronosticos | Comparación de pronósticos (HU-07) | FICTICIO | Fiorella | 2026-09-14 | 30 | [KPI-1](../indicadores/KPI-1-mejora-mae-pronostico.md) |
| historial_movimientos | Historial de doce meses con precios (HU-30) | FICTICIO | Samuel | 2026-09-14 | 1220 | [KPI-1](../indicadores/KPI-1-mejora-mae-pronostico.md), [KPI-3](../indicadores/KPI-3-vigencia-datos.md) |
| cotizaciones_proveedor | Cotizaciones de proveedores (HU-31) | FICTICIO | Samuel | 2026-09-26 | 30 | |
| costos_complementarios | Seguro y otros costos (HU-31) | FICTICIO | Samuel | 2026-09 | 4 | |
| costos_importacion | Costos de importación con respaldo (HU-31) | MIXTO | Samuel | 2026-10-09 | 15 | [KPI-2](../indicadores/KPI-2-costo-con-respaldo.md) |
| ine_flete_mensual | Importaciones de repuestos por mes (INE) | PUBLICO | Samuel | 2026-08 | 2842 | insumo de F05 |
| flete_referencias | Cotizaciones de referencia de flete | PUBLICO | Samuel | 2026-10-09 | 6 | insumo de F05 |
| tc_series_diaria | Tipo de cambio diario (HU-32) | PUBLICO | Equipo (HU-32) | 2026-10-26 | 127 | |
| ventas_simuladas | Ventas diarias por repuesto (HU-34) | FICTICIO | Equipo (HU-34) | 2026-10-24 | 19860 | ver ambigüedad de [KPI-3](../indicadores/KPI-3-vigencia-datos.md) |
| compras_simuladas | Compras recibidas (HU-34) | FICTICIO | Equipo (HU-34) | 2026-10-23 | 3600 | |
| inventario_simulado | Inventario diario (HU-34) | FICTICIO | Equipo (HU-34) | 2026-10-24 | 19860 | |

## Observaciones

- [OBSERVADO] Las fechas de corte no coinciden entre conjuntos: van de 2026-08 (INE) a 2026-10-26 (tipo de cambio) ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`). El manifiesto ya lo anota como limitación.
- [OBSERVADO] Los conjuntos de la HU-34 (ventas, compras e inventario simulados) llegan al 23 y 24 de octubre, mientras que los movimientos de la HU-17 y la HU-30 llegan al 14 de septiembre. Esto afecta la definición de [KPI-3](../indicadores/KPI-3-vigencia-datos.md).
- [OBSERVADO] El campo `fecha_corte_datos` de `historial_ajustes` trae hora (`2026-10-02 10:05:00`) y el de `costos_complementarios` sólo mes (`2026-09`): el formato no es uniforme.

## Contradicciones

- **C-03. Clase de los datos de la HU-32.** [OBSERVADO] F06 describe la HU-32 como «MIXTO: tipo de cambio oficial del BCB (público) y tipo de cambio pagado por la empresa (FICTICIO)» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla «Historias de usuario terminadas», fila HU-32). F02 registra el único conjunto de esa historia, `tc_series_diaria`, como PUBLICO ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `tc_series_diaria`, columna `tipo_dato`). **Prevalece F02 para la clase de `tc_series_diaria`** [INFERENCIA]: es el registro de origen y el manifiesto dice que F06 sólo resume. Queda **pendiente** saber si la parte FICTICIA de la HU-32 (tipo de cambio pagado) es un conjunto que el registro no incluye. Ningún indicador usa este conjunto.
- **C-04. Clase de la tabla de costos de importación.** Ver [F05](F05-costos-importacion-hu31.md#contradicciones).

## Cómo recalcular

    python3 -c "import csv,collections;r=list(csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8')));print(len(r),collections.Counter(x['tipo_dato'] for x in r),collections.Counter(x['estado_ultima_carga'] for x in r))"
