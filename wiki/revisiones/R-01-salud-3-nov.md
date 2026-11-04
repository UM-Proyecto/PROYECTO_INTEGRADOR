---
tipo: hallazgo
subtipo: revision
fuentes: [F01, F02, F03, F04, F05, F06]
fecha: 2026-10-27
clase_datos: [FICTICIO, PUBLICO, MIXTO]
estado: inferido
revision: borrador
actualizado: 2026-11-03
tags: [hallazgo, revision, ficticio, publico, mixto]
---

# R-01. Revisión de salud de la wiki al 3-nov-2026

**Etapa:** 3, revisión de salud. **Alcance:** las 16 páginas de `wiki/` y [[AGENTS]], contrastadas con los 14 archivos de `fuentes/`. **Páginas que la motivan:** [[index]], [[objetivos]], [[Q-01-criterios-hu33-al-3-nov|Q-01]] y todas las de fuentes, indicadores y síntesis.

> Esta revisión corrige páginas que sostienen la respuesta a la pregunta de negocio. Queda en borrador hasta la revisión humana. Las cifras sobre datos FICTICIOS que aparecen acá prueban métodos; no describen a MULTIPARTES.

## Controles automáticos

[OBSERVADO] Antes de corregir nada, `python3 src/u4-t1/salud.py` dio 0 en sus once controles sobre 16 páginas: enlaces y wikilinks rotos, páginas huérfanas, páginas fuera del índice, metadatos, campos de indicador, cifras sin etiqueta, etiquetas sin cita, frases prohibidas, títulos y nombres duplicados. `python3 src/u4-t1/manifiesto.py` dio 14 de 14 copias intactas ([manifiesto](../../fuentes/MANIFIESTO.csv)).

[INFERENCIA] Que los controles den cero no significa que la wiki esté sana. `salud.py` mira la forma: si una cifra tiene etiqueta, si un enlace resuelve. No compara lo que dice una página con lo que dice otra o con la fuente, no revisa afirmaciones sin cifra y no sabe si una fecha está vieja. Los hallazgos de abajo salen de leer cada página contra `fuentes/`, y ninguno lo detectaba el script.

## Cifras verificadas

[CALCULADO] Se recalcularon desde `fuentes/` todas las cifras de los indicadores y de las páginas de fuentes con los comandos de cada página. Coinciden: 17 conjuntos (13 FICTICIO, 3 PUBLICO, 1 MIXTO) y sus cortes y conteos en [F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv); 30 filas, 30 SIN_SELECCION_FIABLE, MAE medio de 0,14, 0,14 y 0,32, y 0,467 en los 3 repuestos con ventas, en [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv); 6, 5 y 4 componentes por respaldo y los valores de flete en [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv); 42 días de línea base y 50 al 3-nov-2026 para KPI-3. Las citas textuales de F01, F03, F04 y F06 se compararon con el texto de cada archivo y también coinciden.

## Hallazgos

| Código | Tipo | Página | Qué pasa | Estado |
|---|---|---|---|---|
| H-01 | Cifra inconsistente | [[O-3-datos-al-dia|O-3]] | Decía que hace falta un corte «posterior al 2026-10-04». Con corte el 2026-10-04 son exactamente 30 días y la meta (≤ 30) se cumple, como dicen [[KPI-3-vigencia-datos|KPI-3]] y Q-01 | Corregido |
| H-02 | Contradicción nueva | [[F05-costos-importacion-hu31#Contradicciones|F05]], [[KPI-2-costo-con-respaldo|KPI-2]], [[index]] | La resolución de C-04 explica el MIXTO de la tabla de costos de una forma que no coincide con la definición de MIXTO del manifiesto y de F06 | Registrada como C-05, pendiente |
| H-03 | Error de hecho | [[F05-costos-importacion-hu31#Contradicciones|F05]], [[F06-portada-repositorio|F06]], [[index]] | C-04 decía que la HU-31 tiene dos conjuntos; F02 le registra tres | Corregido |
| H-04 | Vacío no anotado | [[O-2-cuanto-cuesta-traerlo|O-2]], [[KPI-2-costo-con-respaldo|KPI-2]] | F02 registra un conjunto FICTICIO de «seguro y otros costos de importación» que la wiki no mencionaba al decir que no hay datos de seguro | Corregido |
| H-05 | Lectura incompleta | [[KPI-1-mejora-mae-pronostico|KPI-1]], [[F04-pronosticos-hu07|F04]], [[O-1-cuanto-se-vendera|O-1]] | La wiki atribuía la falta de selección sólo al largo del historial; los 30 casos también fallan la regla de tres días con ventas en entrenamiento | Corregido |
| H-06 | Afirmación inexacta | [[F06-portada-repositorio|F06]], [[KPI-3-vigencia-datos|KPI-3]] | La página de F06 decía que no hay diferencia con F03 en los criterios; hay tres diferencias de redacción, una de ellas relevante para KPI-3 | Corregido |
| H-07 | Etiqueta equivocada | [[objetivos]], [[KPI-2-costo-con-respaldo|KPI-2]] | «No medible» iba como [OBSERVADO] (es una conclusión) y 10 / 15 = 66,7 % como [INFERENCIA] (es un cálculo) | Corregido |
| H-08 | Afirmaciones sin etiqueta | O-1, O-2, O-3, KPI-1, KPI-3 | Once ítems de «Qué falta» y «Ambigüedades» sin etiqueta; `salud.py` no los marca porque no tienen cifra | Corregido |
| H-09 | Datos desactualizados | [[O-3-datos-al-dia|O-3]], [[KPI-2-costo-con-respaldo|KPI-2]] | El corte de un conjunto esconde filas más viejas: `flete_referencias` figura al 2026-10-09, pero 5 de sus 6 filas son de 2026-06 | Corregido (anotado) |
| H-10 | Nota vencida en página revisada | [[Q-01-criterios-hu33-al-3-nov|Q-01]] | El aviso del principio dice que la respuesta «queda en borrador hasta la revisión humana», pero la página ya tiene `revision: revisado` | Pendiente |
| H-11 | Convención ambigua | Todas | `fecha` es «el corte de los datos que usa la página», pero las páginas con varios cortes eligen distinto | Pendiente |
| H-12 | Instrucción incompleta | [[AGENTS]] | La regla del prefijo de las citas no nombraba `wiki/consultas/` ni `wiki/revisiones/` | Corregido |
| H-13 | Índice desactualizado | [[index]] | La sección «Revisiones» decía «Todavía no hay» | Corregido |

### H-01. Fecha límite del corte de movimientos

[CALCULADO] 2026-11-03 − 2026-10-04 = 30 días, y la meta es «30 días o menos» ([F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 3). Un corte el mismo 2026-10-04 ya cumple, así que «posterior al 2026-10-04» dejaba afuera el día límite. [[O-3-datos-al-dia|O-3]] dice ahora «el 2026-10-04 o después», igual que KPI-3 y Q-01.

### H-02. Qué hace MIXTA a la tabla de costos (C-05)

[OBSERVADO] El manifiesto define MIXTO como «tablas que combinan datos públicos con datos de prueba» ([manifiesto](../../fuentes/MANIFIESTO.md), «Cómo se clasifican los datos»), y F06 dice que los costos de la HU-31 «combinan las fuentes públicas con datos FICTICIOS de la empresa» ([F06](../../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»). La tabla de costos tiene 6 filas con valores publicados, 5 estimaciones calculadas sobre datos del INE y 4 filas sin valor ([F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columnas `tipo_dato`, `respaldo` y `valor_min`); ninguna fila trae datos de prueba.

[INFERENCIA] La revisión 01 cerró C-04 diciendo que la tabla «es MIXTO por combinar datos publicados y estimaciones sobre datos del INE». Ese motivo no aparece en ninguna fuente: con la definición del manifiesto, una tabla sin datos de prueba sería PUBLICO. La clase registrada sigue siendo MIXTO, porque para la clase de un conjunto prevalece F02 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `costos_importacion`), pero la explicación de la wiki queda sin respaldo. Hay dos salidas posibles: que F02 deba decir PUBLICO, o que el equipo cuente las estimaciones de la HU-31 como dato propio y no público. Queda **pendiente** de que decida Samuel Castillo, responsable del conjunto. No cambia el valor de KPI-2; sí cambia cómo se describe la clase de sus datos en KPI-2, O-2 y Q-01.

[INFERENCIA] C-04 no se reabre. Lo que resolvió sigue en pie: la fila HU-31 de F06 describe la historia entera, no sólo la tabla. C-05 cuestiona solamente el motivo que la resolución dio para el MIXTO.

### H-03. Los conjuntos de la HU-31 son tres

[OBSERVADO] F02 registra tres conjuntos de la HU-31, todos a cargo de Samuel: `cotizaciones_proveedor` (FICTICIO, 30 registros), `costos_complementarios` (FICTICIO, 4 registros) y `costos_importacion` (MIXTO, 15 registros) ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columnas `conjunto`, `fuente` y `tipo_dato`). La resolución de C-04 hablaba de «dos conjuntos». Se corrigió en F05, F06 y el índice. Las entradas anteriores del log, que también dicen dos, no se editan; esta revisión deja la corrección.

### H-04. Un conjunto FICTICIO de seguro y otros costos

[OBSERVADO] `costos_complementarios` se describe como «Seguro y otros costos de importación», tiene 4 registros con columnas `concepto`, `valor`, `unidad` y `fecha_dato`, y corte 2026-09 ([F02](../../fuentes/F02_registro_fuentes_HU02/conjuntos.csv), fila `costos_complementarios`). El archivo no está en `fuentes/`.

[INFERENCIA] Cuatro registros de seguro y otros costos, frente a cuatro componentes PENDIENTE, sugieren que el equipo generó valores de prueba para esos mismos componentes, pero sin el archivo no se puede comprobar. Si fuera así, no mejoraría KPI-2: un valor FICTICIO no es un documento de respaldo. O-2 decía «no hay ningún dato» de esos componentes; ahora dice que no hay ninguno en la tabla de costos y menciona este conjunto.

### H-05. Por qué ningún método queda seleccionado

[CALCULADO] Las 30 filas de F04 traen en `limitaciones` el texto «menos de 3 dias con ventas en entrenamiento». En `dias_con_ventas_entrenamiento`, 8 de los 10 repuestos tienen 0 y 2 tienen 1 ([F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columnas `limitaciones` y `dias_con_ventas_entrenamiento`, filas `ultimo_periodo`). Los 3 repuestos con ventas en la evaluación tienen 1 día con ventas cada uno y ninguno en entrenamiento.

[INFERENCIA] El README de F04 exige, además de 12 + 12 meses, «tres días con ventas en entrenamiento» ([F04](../../fuentes/F04_pronosticos_HU07/README.md), quinto párrafo). Ningún repuesto cumple esa regla, así que la falta de selección no viene sólo del largo del historial: también hay pocas ventas. El empate en 0,467 se explica igual. Si un repuesto no vendió nada en entrenamiento, los tres métodos pronostican cero para la evaluación y el MAE de cada uno es simplemente lo que se vendió. Sobre datos FICTICIOS esto prueba el método y no describe la demanda de MULTIPARTES.

### H-06. F06 resume los criterios con otras palabras

[OBSERVADO] En los criterios, F06 se aparta de F03 en tres puntos ([F06](../../fuentes/F06_portada_repositorio/README.md), «Criterios de éxito (HU-33)»; [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), tabla principal). En el criterio 1 la meta es «15 % menos de error», sin la condición de un año de historial y 3 meses reservados. La línea base del mismo criterio dice «falta un año de historial» donde F03 dice «HU-07 solo cubre del 1 al 14 de septiembre». Y el criterio 3 habla de «la fecha de los datos», no de «los datos de movimientos».

[INFERENCIA] No es una contradicción: F06 resume y prevalece F03 ([manifiesto](../../fuentes/MANIFIESTO.md), fila F06). Pero la tercera diferencia importa para la ambigüedad 1 de KPI-3. Leída como F06, «la fecha de los datos» admite cualquier conjunto, incluidos los de la HU-34 al 24-oct. Se agregó a esa ambigüedad.

### H-09. Antigüedad de cada corte al 3-nov-2026

[CALCULADO] Días entre el 3-nov-2026 y el corte de cada conjunto. Cuando el corte es un mes, se toma el último día del mes, lo que da la antigüedad mínima ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), columna `fecha_corte_datos`; comando abajo):

| Conjunto | Clase | Corte | Días al 3-nov | Lo usa |
|---|---|---|---|---|
| movimientos_inventario, reporte_depuracion, historial_movimientos, comparacion_pronosticos | FICTICIO | 2026-09-14 | 50 | KPI-1, KPI-3 |
| stock_inicial | FICTICIO | 2026-08-31 | 64 | |
| ine_flete_mensual | PUBLICO | 2026-08 | 64 o más | estimaciones de KPI-2 |
| cotizaciones_proveedor | FICTICIO | 2026-09-26 | 38 | |
| costos_complementarios | FICTICIO | 2026-09 | 34 o más | |
| conteos_fisicos | FICTICIO | 2026-09-30 | 34 | |
| historial_ajustes | FICTICIO | 2026-10-02 | 32 | |
| costos_importacion, flete_referencias | MIXTO, PUBLICO | 2026-10-09 | 25 | KPI-2 |
| compras_simuladas | FICTICIO | 2026-10-23 | 11 | |
| ventas_simuladas, inventario_simulado | FICTICIO | 2026-10-24 | 10 | ambigüedad de KPI-3 |
| tc_series_diaria | PUBLICO | 2026-10-26 | 8 | |

[CALCULADO] El corte de `flete_referencias` (2026-10-09) es el del índice SCFI. Las 5 cotizaciones del agente de carga, que son 5 de los 6 respaldos DOCUMENTADO de KPI-2, tienen fecha 2026-06 y una página modificada el 2026-06-02: 154 días al 3-nov-2026 ([F05](../../fuentes/F05_costos_importacion_HU31/flete_referencias_puntuales.csv), columnas `fecha_dato` y `nota`). [INFERENCIA] Si se mira sólo el corte del conjunto, los respaldos parecen más nuevos de lo que son. Se anotó en KPI-2 (ambigüedad 3) y en O-3.

[INFERENCIA] Ninguna página de la wiki usa un valor que haya cambiado entre la línea base del 26-oct y el 3-nov-2026: la única carga registrada es del 27-oct ([F02](../../fuentes/F02_registro_fuentes_HU02/historial_cargas.csv), columna `fecha_intento`) y F05 no cambió (misma huella). Lo único que se mueve con el calendario es KPI-3, que sube un día por día y ya está recalculado al 3-nov.

## Pendientes y por qué quedan así

- **H-02 / C-05.** Sólo el equipo puede decir si `costos_importacion` es MIXTO o PUBLICO; la wiki no corrige la clase de F02 por su cuenta.
- **H-10.** [[Q-01-criterios-hu33-al-3-nov|Q-01]] tiene `revision: revisado`, que pone la revisión humana. El agente no edita una página revisada, porque el cambio quedaría bajo una aprobación que no lo cubre. Hay que actualizar el aviso del principio y, si se acepta C-05, la columna de clase de KPI-2.
- **H-11.** `index.md` usa la fecha de la carga (2026-10-27), `objetivos.md` y Q-01 el corte de la tabla de costos (2026-10-09), y las síntesis y los indicadores el corte de su conjunto. [INFERENCIA] Propuesta para el equipo: en las páginas que combinan varios conjuntos, `fecha` es el corte más antiguo entre los datos que sostienen sus conclusiones (para Q-01 y objetivos, 2026-09-14). No se aplicó porque cambia la convención de [[AGENTS]] y afecta todas las páginas.
- **Sin cambio.** C-02 y C-03 siguen pendientes por los motivos que dan sus páginas. La regla de agregación de KPI-1 y el conjunto de movimientos de KPI-3 siguen sin fijar.
- **Observado sin corregir.** El log tiene dos entradas de la etapa 2: una del agente y otra de la corrida 02 con su revisión humana. Las entradas anteriores no se editan, así que quedan las dos; la segunda es la que vale.
- **Redundancia aceptada.** Los comandos de KPI-1, KPI-2 y KPI-3 se repiten en Q-01 con pequeñas diferencias. No son páginas duplicadas, pero si cambia un comando hay que cambiarlo en los dos lugares.

## Cómo recalcular

Controles automáticos:

    python3 src/u4-t1/salud.py
    python3 src/u4-t1/manifiesto.py

H-05, días con ventas en entrenamiento y filas con la limitación:

    python3 -c "import csv;f=list(csv.DictReader(open('fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv',encoding='utf-8-sig')));print({x['codigo_unico']:x['dias_con_ventas_entrenamiento'] for x in f if x['metodo']=='ultimo_periodo'},sum('menos de 3 dias con ventas en entrenamiento' in x['limitaciones'] for x in f))"

H-09, antigüedad de cada corte al 3-nov-2026:

    python3 -c "import csv,datetime as d,calendar as k;h=d.date(2026,11,3);f=lambda c:d.date(int(c[:4]),int(c[5:7]),k.monthrange(int(c[:4]),int(c[5:7]))[1]) if len(c)==7 else d.date.fromisoformat(c[:10]);print({x['conjunto']:(h-f(x['fecha_corte_datos'])).days for x in csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8')) if x['fecha_corte_datos']})"
