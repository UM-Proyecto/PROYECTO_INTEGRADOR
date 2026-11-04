---
tipo: fuente
fuentes: [F06, F02, F03]
fecha_datos: 2026-11-03
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: borrador
actualizado: 2026-11-03
---

# F06. Portada del repositorio del equipo

**Archivo:** [`README.md`](../../fuentes/F06_portada_repositorio/README.md) de `UM-Proyecto/MINERIA_DATOS`, commit `c27757a` del 3-nov-2026.

F06 resume a las demás fuentes. Según el manifiesto, ante una diferencia manda el archivo de origen. La wiki la usa para el origen de los datos, la lista de historias de usuario y sus responsables.

## Qué dice

- [OBSERVADO] Origen de los datos: «MULTIPARTES facilitó una muestra inicial pequeña, de unos 20 registros. Para poder aplicar y comparar las técnicas, el equipo la amplió con datos de prueba con la misma estructura» ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «De dónde salen los datos», FICTICIOS).
- [OBSERVADO] Son PUBLICOS los fletes (INE, agente de carga, SCFI) y el tipo de cambio oficial del BCB; son MIXTOS los costos de importación de la HU-31 y la comparación del tipo de cambio de la HU-32 ([F06](../../fuentes/F06_portada_repositorio/README.md), misma sección).
- [OBSERVADO] Repite los tres criterios de la HU-33 con las mismas metas y líneas base que F03: 15 %, 80 % y 30 días; «sin método elegible», «6 de 15 componentes (40 %)» y «42 días» ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «Criterios de éxito (HU-33)»). [INFERENCIA] No hay diferencia con [F03](F03-criterios-exito-hu33.md).
- [OBSERVADO] La tabla de historias lista 13 entradas (de la pregunta enfocada a la HU-36), con responsable y clase de datos ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «Historias de usuario terminadas»). Las que alimentan la wiki: HU-02 (Samuel), HU-07 (Fiorella), HU-30 y HU-31 (Samuel), HU-33 (Samuel).
- [OBSERVADO] La HU-36, «Repetición de los pronósticos con 284 días de historial», figura con código y resultado «Pendiente de subir» y documento «Resultado comentado en Jira» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla «Historias de usuario terminadas», fila HU-36).

## Para qué sirve en la wiki

- [INFERENCIA] Es la referencia contra la que se comparan otras fuentes cuando describen el origen de los datos. Si una fuente dijera que la empresa «no entregó» datos, la diferencia con esta sección iría a «Contradicciones». En F01 a F05 no aparece esa expresión; F05 habla de «Cuando la empresa entregue un historial más amplio» ([F05](../../fuentes/F05_costos_importacion_HU31/LEEME_hu30-31.md), título de la última sección), que es compatible con F06.

## Contradicciones

- **C-03.** F06 dice que la HU-32 es MIXTO; F02 registra su conjunto como PUBLICO. Ver [F02](F02-registro-fuentes-hu02.md#contradicciones).
- **C-04 (resuelta).** La fila HU-31 de F06 describe la historia entera, con dos conjuntos; las cotizaciones FICTICIAS no están en la tabla de costos sino en `cotizaciones_proveedor`. Ver [F05](F05-costos-importacion-hu31.md#contradicciones).

## Privacidad

F06 nombra al docente y enlaza al tablero Jira del equipo. La wiki no copia esos datos.
