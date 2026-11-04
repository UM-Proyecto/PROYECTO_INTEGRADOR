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

## 2026-11-03. Etapa 2: consulta

**Fuentes leídas:** `fuentes/MANIFIESTO.md`, F02 (`registro_actualizaciones.csv`), F03 (`CRITERIOS_APROBADOS.md`), F04 (`comparacion_pronosticos.csv`), F05 (`hu31_costos_importacion.csv`) y F06 (`README.md`), además de [[index]], [[objetivos]], los tres indicadores y las tres síntesis.

**Pregunta:** qué criterios de la HU-33 respaldan hoy una decisión de compra, con qué valor frente a su meta y qué falta.

**Respuesta:** ninguno. KPI-1 no es medible (30 de 30 combinaciones sin selección, datos FICTICIOS); KPI-2 da 40 % frente a 80 % (MIXTO, valores PUBLICOS); KPI-3 da 50 días frente a 30 (FICTICIO). Detalle en [[Q-01-criterios-hu33-al-3-nov|Q-01]]. Las cifras se recalcularon desde `fuentes/` y coinciden con las de las páginas de indicador.

**Creadas:** `wiki/consultas/Q-01-criterios-hu33-al-3-nov.md`.

**Modificadas:** `wiki/index.md` (sección Consultas), `wiki/objetivos.md` (enlace a la consulta en «Lectura conjunta»), `wiki/log.md`.

**Pendientes:**

- C-02 sigue pendiente; el conjunto de movimientos de KPI-3 y la regla de agregación de KPI-1 siguen sin fijar.
- La HU-36 (284 días) no está en `fuentes/`, y aunque llegara no alcanza el año más 3 meses de F03.
- Q-01 queda en `revision: borrador` hasta la revisión humana.

## 2026-11-03. Etapa 2: consulta (corrida 02) y revisión humana

**Agente:** Claude Code (Claude Opus 5.5), prompt mejorado versión 2. Creó [[Q-01-criterios-hu33-al-3-nov|Q-01]] y la enlazó desde [[index]] y [[objetivos]].

**Respuesta:** ninguno de los tres criterios de la HU-33 respalda hoy una decisión de compra. KPI-1 no es medible, KPI-2 está en 40 % frente a 80 % y KPI-3 en 50 días frente a 30.

**Revisión humana (notas en `docs/u4-t1/evidencia/revisiones/02.md`):** se verificaron tres afirmaciones de la respuesta contra `fuentes/` con `src/u4-t1/verificar.py` (Q1 a Q3). Las cifras coinciden. La lectura de KPI-1 estaba incompleta: el −128,6 % de «mismo día de la semana» no muestra que ese método sea peor, porque en los 3 repuestos con ventas los tres métodos empatan en 0,467 y toda la diferencia sale de dos repuestos sin ventas. Se corrigió en Q-01, [[KPI-1-mejora-mae-pronostico|KPI-1]], [[F04-pronosticos-hu07|F04]] y [[O-1-cuanto-se-vendera|O-1]]. También se precisó que las 5 estimaciones de KPI-2 son cálculos sobre datos públicos, no valores publicados. Q-01 queda como revisada.

## 2026-11-03. Etapa 3: revisión de salud

**Agente:** Claude Code (Claude Opus 5.5), prompt mejorado versión 2.

**Fuentes leídas:** `fuentes/MANIFIESTO.md` y `MANIFIESTO.csv`, F01 (texto del docx), F02 (los cuatro archivos), F03 (aprobados y borrador), F04 (CSV y README), F05 (los cuatro archivos) y F06. También las 16 páginas de la wiki y [[AGENTS]].

**Controles:** `salud.py` dio 0 hallazgos antes y después de los cambios; `manifiesto.py`, 14 de 14 copias intactas. Todas las cifras de la wiki se recalcularon desde `fuentes/` y coinciden.

**Hallazgos:** 13, en [[R-01-salud-3-nov|R-01]]. Diez quedaron corregidos: un día de diferencia en el corte que pide O-3, la HU-31 con tres conjuntos y no dos, `costos_complementarios` sin mencionar, la regla de tres días con ventas en entrenamiento que ningún repuesto cumple, la redacción de F06 frente a F03, dos etiquetas equivocadas, once afirmaciones sin etiqueta, la antigüedad de las cotizaciones, el prefijo de citas en AGENTS.md y la sección de revisiones del índice. Tres quedan pendientes.

**Creadas:** `wiki/revisiones/R-01-salud-3-nov.md`.

**Modificadas:** `AGENTS.md` (prefijo de citas, sección «Revisión de salud»), `wiki/index.md` (C-04, C-05, ambigüedades, revisiones), `wiki/objetivos.md`, `wiki/fuentes/F04-pronosticos-hu07.md`, `F05-costos-importacion-hu31.md`, `F06-portada-repositorio.md`, `wiki/indicadores/KPI-1-mejora-mae-pronostico.md`, `KPI-2-costo-con-respaldo.md`, `KPI-3-vigencia-datos.md`, `wiki/sintesis/O-1-cuanto-se-vendera.md`, `O-2-cuanto-cuesta-traerlo.md`, `O-3-datos-al-dia.md`, `wiki/log.md`. Cada página modificada tiene una sección «Cambios». No cambió ningún valor de indicador ni ningún estado frente a la meta.

**Contradicción nueva:** C-05, la tabla de costos es MIXTO en F02 pero no trae datos de prueba, que es lo que define MIXTO en el manifiesto y en F06. Pendiente del equipo.

**Pendientes:**

- C-05, C-02 y C-03; la regla de agregación de KPI-1 y el conjunto de movimientos de KPI-3.
- [[Q-01-criterios-hu33-al-3-nov|Q-01]] está revisada y el agente no la edita: su aviso inicial todavía dice que queda en borrador y, si se acepta C-05, cambia la clase de KPI-2 en su tabla.
- Convención del campo `fecha` en páginas con varios cortes: propuesta en R-01, sin aplicar.
- R-01 y las páginas modificadas quedan en `revision: borrador` hasta la revisión humana.
