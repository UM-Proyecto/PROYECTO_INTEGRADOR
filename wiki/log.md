---
tipo: log
fuentes: [F01, F02, F03, F04, F05, F06]
fecha_datos: 2026-10-27
clase_datos: []
estado: borrador
actualizado: 2026-11-03
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
