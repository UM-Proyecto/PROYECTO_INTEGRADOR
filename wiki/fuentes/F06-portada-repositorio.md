---
tipo: fuente
subtipo: fuente
fuentes: [F06, F02, F03]
fecha: 2026-11-03
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: observado
revision: borrador
actualizado: 2026-11-03
tags: [fuente, ficticio, publico, mixto]
---

# F06. Portada del repositorio del equipo

**Archivo:** [`README.md`](../../fuentes/F06_portada_repositorio/README.md) de `UM-Proyecto/MINERIA_DATOS`, commit `c27757a` del 3-nov-2026.

F06 resume a las demás fuentes. Según el manifiesto, ante una diferencia manda el archivo de origen. La wiki la usa para el origen de los datos, la lista de historias de usuario y sus responsables.

## Qué dice

- [OBSERVADO] Origen de los datos: «MULTIPARTES facilitó una muestra inicial pequeña, de unos 20 registros. Para poder aplicar y comparar las técnicas, el equipo la amplió con datos de prueba con la misma estructura» ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «De dónde salen los datos», FICTICIOS).
- [OBSERVADO] Son PUBLICOS los fletes (INE, agente de carga, SCFI) y el tipo de cambio oficial del BCB; son MIXTOS los costos de importación de la HU-31 y la comparación del tipo de cambio de la HU-32 ([F06](../../fuentes/F06_portada_repositorio/README.md), misma sección).
- [OBSERVADO] Repite los tres criterios de la HU-33 con las mismas cifras que F03: 15 %, 80 % y 30 días; «sin método elegible», «6 de 15 componentes (40 %)» y «42 días» ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «Criterios de éxito (HU-33)»). La redacción cambia en tres puntos. En el criterio 1 la meta no dice «con un año de historial y 3 meses reservados», y la línea base dice «falta un año de historial» donde F03 dice «HU-07 solo cubre del 1 al 14 de septiembre». El criterio 3 habla de «la fecha de los datos», no de «los datos de movimientos» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal). [INFERENCIA] No es una contradicción: F06 resume y prevalece [[F03-criterios-exito-hu33|F03]]. La tercera diferencia se anota en la ambigüedad 1 de [[KPI-3-vigencia-datos#Ambigüedades|KPI-3]].
- [OBSERVADO] La tabla de historias lista 13 entradas (de la pregunta enfocada a la HU-36), con responsable y clase de datos ([F06](../../fuentes/F06_portada_repositorio/README.md), sección «Historias de usuario terminadas»). Las que alimentan la wiki: HU-02 (Samuel), HU-07 (Fiorella), HU-30 y HU-31 (Samuel), HU-33 (Samuel).
- [OBSERVADO] La HU-36, «Repetición de los pronósticos con 284 días de historial», figura con código y resultado «Pendiente de subir» y documento «Resultado comentado en Jira» ([F06](../../fuentes/F06_portada_repositorio/README.md), tabla «Historias de usuario terminadas», fila HU-36).

## Para qué sirve en la wiki

- [INFERENCIA] Es la referencia contra la que se comparan otras fuentes cuando describen el origen de los datos. Si una fuente dijera que la empresa «no entregó» datos, la diferencia con esta sección iría a «Contradicciones». En F01 a F05 no aparece esa expresión; F05 habla de «Cuando la empresa entregue un historial más amplio» ([F05](../../fuentes/F05_costos_importacion_HU31/LEEME_hu30-31.md), título de la última sección), que es compatible con F06.

## Contradicciones

- **C-03.** F06 dice que la HU-32 es MIXTO; F02 registra su conjunto como PUBLICO. Ver [[F02-registro-fuentes-hu02#Contradicciones|F02]].
- **C-04 (resuelta).** La fila HU-31 de F06 describe la historia entera, que en F02 tiene tres conjuntos; las cotizaciones FICTICIAS no están en la tabla de costos sino en `cotizaciones_proveedor`. Ver [[F05-costos-importacion-hu31#Contradicciones|F05]].
- **C-05 (pendiente).** F06 dice que los costos de la HU-31 «combinan las fuentes públicas con datos FICTICIOS de la empresa» ([F06](../../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»), pero la tabla de costos, que F02 registra como MIXTO, no trae datos de prueba. Ver [[F05-costos-importacion-hu31#Contradicciones|F05]].

## Privacidad

F06 nombra al docente y enlaza al tablero Jira del equipo. La wiki no copia esos datos.

## Cambios

- 2026-11-03, revisión de salud [[R-01-salud-3-nov|R-01]]: «No hay diferencia con F03» pasó a describir las tres diferencias de redacción (H-06). En C-04, «dos conjuntos» pasó a «tres» (H-03). Se agregó C-05 (H-02).
