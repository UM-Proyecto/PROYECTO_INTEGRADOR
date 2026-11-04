---
tipo: fuente
fuentes: [F01]
fecha_datos: 2026-10-14
clase_datos: []
estado: borrador
actualizado: 2026-11-03
---

# F01. Pregunta enfocada y objetivo general

**Archivo:** [`PREGUNTA ENFOCADA Y OBJETIVO.docx`](../../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx) · **Origen:** `UM-Proyecto/MINERIA_DATOS`, commit `c27757a`, ruta `docs/pregunta-enfocada/` · **Historia:** SCRUM-37, redactada por Fiorella Sandoval · **Fecha del documento:** 14-oct-2026.

No contiene datos; describe la pregunta y el objetivo del proyecto. Por eso no tiene clase FICTICIO, PUBLICO ni MIXTO.

## Qué dice

- [OBSERVADO] Pregunta enfocada: «¿Qué técnicas de análisis de datos permiten apoyar las decisiones de compra de la empresa MULTIPARTES de Santa Cruz de la Sierra durante el segundo semestre del 2026?» ([F01](../../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), sección «Pregunta Enfocada»).
- [OBSERVADO] Objetivo general enfocado: «Determinar las técnicas de análisis de datos que permiten apoyar las decisiones de compra de la empresa MULTIPARTE durante el segundo semestre del 2026.» ([F01](../../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), sección «Objetivo general enfocado»).
- [OBSERVADO] La portada fecha el documento el 14 de octubre de 2026 y lo ubica en Minería de Datos, VI semestre 2026 ([F01](../../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), portada).

## Cómo se usa en la wiki

- [INFERENCIA] F01 fija el objetivo general pero no nombra al usuario ni la decisión concreta. La wiki lo divide en tres objetivos (O1, O2, O3), uno por cada criterio aprobado en la HU-33 ([F03](F03-criterios-exito-hu33.md)). El mapa está en [objetivos.md](../objetivos.md).
- [INFERENCIA] F01 no define indicadores ni metas; esos vienen de F03.

## Contradicciones

- **C-01. Nombre de la empresa.** [OBSERVADO] El objetivo escribe «MULTIPARTE» y la pregunta, en el mismo documento, «MULTIPARTES» ([F01](../../fuentes/F01_pregunta_enfocada/PREGUNTA%20ENFOCADA%20Y%20OBJETIVO.docx), secciones «Pregunta Enfocada» y «Objetivo general enfocado»). La portada del repositorio usa «MULTIPARTES» ([F06](../../fuentes/F06_portada_repositorio/README.md), título y «Pregunta enfocada»). **Prevalece «MULTIPARTES»** [INFERENCIA]: es la forma que usan la pregunta, F03, F06 y el manifiesto; «MULTIPARTE» parece una errata y no cambia el sentido.

## Cómo leerla

    python3 -c "import zipfile,re;x=zipfile.ZipFile('fuentes/F01_pregunta_enfocada/PREGUNTA ENFOCADA Y OBJETIVO.docx').read('word/document.xml').decode();print('\n'.join(t for t in (''.join(re.findall(r'<w:t[^>]*>([^<]*)</w:t>',p)) for p in re.findall(r'<w:p[ >].*?</w:p>',x,re.S)) if t.strip()))"
