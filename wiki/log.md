---
tipo: registro
subtipo: log
fuentes: [F01, F02, F03, F04, F05, F06]
fecha: 2026-10-27
clase_datos: []
estado: observado
revision: borrador
actualizado: 2026-11-03
tags: [registro]
---

# Registro de la wiki

Registro cronológico. Sólo se agregan entradas al final; las anteriores no se editan.

## 2026-11-03. Etapa 1: estructura e ingesta inicial

**Agente:** Claude Code (Claude Opus 5.5).

**Fuentes leídas:** `fuentes/MANIFIESTO.md`, `fuentes/MANIFIESTO.csv`, F01 (texto extraído del docx con `zipfile`), F02 (los cuatro archivos), F03 (aprobados y borrador), F04 (CSV y README), F05 (los cuatro archivos), F06.

**Creadas:**

- `AGENTS.md` (raíz)
- `wiki/index.md`, `wiki/log.md`, `wiki/objetivos.md`
- `wiki/fuentes/F01-pregunta-enfocada.md`, `F02-registro-fuentes-hu02.md`, `F03-criterios-exito-hu33.md`, `F04-pronosticos-hu07.md`, `F05-costos-importacion-hu31.md`, `F06-portada-repositorio.md`
- `wiki/indicadores/KPI-1-mejora-mae-pronostico.md`, `KPI-2-costo-con-respaldo.md`, `KPI-3-vigencia-datos.md`
- `wiki/sintesis/O-1-cuanto-se-vendera.md`, `O-2-cuanto-cuesta-traerlo.md`, `O-3-datos-al-dia.md`

**Modificadas:** ninguna (no existía la wiki).

**Valores calculados:** KPI-1 no medible (las 30 filas de F04 sin selección; MAE medio FICTICIO 0,14 / 0,14 / 0,32); KPI-2 = 6 / 15 = 40 %; KPI-3 = 50 días al 3-nov-2026 (línea base 42 al 26-oct). Todos con comando en su página.

**Contradicciones registradas:** C-01 (nombre de la empresa), C-02 (historial para el pronóstico), C-03 (clase de la HU-32), C-04 (MIXTO de la tabla de costos).

**Pendientes:**

- Que el equipo resuelva C-02, C-03 y C-04 y fije el conjunto de movimientos de KPI-3.
- La HU-36 (284 días) y el archivo del INE no están en `fuentes/`.
- Todas las páginas de indicadores, síntesis y objetivos quedan en `estado: borrador` hasta la revisión humana.

## 2026-11-03. Revisión humana de la etapa 1

**Quién:** revisión del equipo sobre la corrida 01. Notas completas y comandos en `docs/u4-t1/evidencia/revisiones/01.md`.

**Recalculado contra `fuentes/`:** las cifras nuevas que trajo el agente (MAE medio de 0,14, 0,14 y 0,32 por método; 7 de 10 repuestos sin ventas en la ventana evaluada; 10 días con `ventas_simuladas`) coinciden. `src/u4-t1/verificar.py` da 5 de 5.

**Corregido:**

- C-04 estaba mal planteada como contradicción pendiente. La fila HU-31 de F06 describe la historia entera, con dos conjuntos; las cotizaciones FICTICIAS son el conjunto `cotizaciones_proveedor`, no la tabla de costos. Queda resuelta en [[F05-costos-importacion-hu31#Contradicciones|F05]], [[F02-registro-fuentes-hu02|F02]], [[F06-portada-repositorio|F06]], [[KPI-2-costo-con-respaldo|KPI-2]], [[O-2-cuanto-cuesta-traerlo|O-2]] e [[index]].
- El agente había marcado como revisadas las seis páginas de fuentes; volvieron a borrador hasta esta revisión.
- Se completaron 24 etiquetas o citas que faltaban en 9 páginas (la primera pasada de `salud.py` marcaba 17 afirmaciones sin cita directa y 10 cifras sin etiqueta).

## 2026-11-03. Compatibilidad con Obsidian

**Pedido del equipo:** que la wiki se abra en Obsidian y se vea en su gráfico, sin dejar de leerse en GitHub.

**Hecho:** `src/u4-t1/obsidian.py` convirtió las 15 páginas. Los enlaces entre páginas pasaron a wikilinks, las citas a `fuentes/` quedaron como enlaces Markdown relativos, y los metadatos pasaron al esquema nuevo (`tipo` por familia, `subtipo`, `fecha`, `estado` como naturaleza del contenido, `revision`, `tags`). Una segunda corrida del conversor no cambia nada. Se versionó `.obsidian/` con `app.json` y `graph.json` (colores por tag: fuente, indicador, hallazgo, decision, moc, registro). Las reglas nuevas están en [[AGENTS]] y en la versión 2 del prompt mejorado.

**Control:** `python3 src/u4-t1/salud.py` da 0 en todos los controles, con 0 wikilinks rotos y 0 páginas huérfanas. Su prueba (`tests/test_salud.py`) arma una wiki con una falla de cada tipo y comprueba que las detecta.
