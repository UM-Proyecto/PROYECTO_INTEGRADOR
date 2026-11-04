# Instrucciones para el agente que mantiene la wiki

Este repositorio (`UM-Proyecto/PROYECTO_INTEGRADOR`) guarda una wiki de conocimiento sobre el proyecto BI de MULTIPARTES, una importadora de repuestos automotrices de Santa Cruz de la Sierra que compra a proveedores de China. La wiki sirve a una decisión concreta: qué repuesto pedir a China, en qué cantidad y cuándo. Quien usa los resultados es el jefe de compras de MULTIPARTES; el equipo (Sabrina Adrian Zelaya, Samuel Castillo y Fiorella Sandoval) mantiene la wiki y los docentes la evalúan.

Escribe en español neutro, sin voseo.

## Qué puedes tocar

- Escribes sólo en `wiki/` y en este archivo.
- `fuentes/`, `data/`, `docs/`, `src/`, `tests/` y `reports/` son de sólo lectura.
- No haces commits. La revisión humana lee el cambio y lo confirma.
- Antes de entregar, comprueba que nada más cambió:

      git status --short
      python3 src/u4-t1/manifiesto.py

## Fuentes

- Lee primero `fuentes/MANIFIESTO.md` y `fuentes/MANIFIESTO.csv`. Sólo valen las fuentes que están ahí (F01 a F06 al 3-nov-2026; puede llegar una F07). No uses internet ni archivos fuera de `fuentes/`.
- Cada fuente tiene una página en `wiki/fuentes/F0N-<tema>.md`. Si una fuente cambia, se copia en una carpeta nueva (por ejemplo `F05b_...`); en la wiki se agrega su página y se actualizan las que dependen de ella, sin borrar la referencia anterior.
- El docx de F01 se lee extrayendo `word/document.xml` con `zipfile` de la biblioteca estándar, sin escribir en `fuentes/`.
- Si un cálculo necesita un script, se escribe fuera del repositorio (por ejemplo en `/tmp`) o como comando de una línea dentro de la página. No se agregan archivos a `src/` ni a `data/`.

## Clases de datos

- Se usan los nombres del registro de la HU-02 (F02, columna `tipo_dato` de `registro_actualizaciones.csv`): FICTICIO, PUBLICO y MIXTO.
- MULTIPARTES facilitó una muestra inicial de unos 20 registros y el equipo la amplió con datos de prueba con la misma estructura. Nunca escribas que la empresa «no entregó» o «no proporcionó» datos. Si una fuente lo dice así, cítala textual y anota la diferencia con F06 en «Contradicciones».
- Un resultado calculado sobre datos FICTICIOS es una prueba del método, no un hecho sobre la empresa. Dilo en la misma frase que el número.
- Toda página que use datos lleva su clase en el bloque de metadatos (`clase_datos`) y en el texto junto a cada cifra.
- Ojo con el nombre de columna: en `hu31_costos_importacion.csv` (F05) la columna `tipo_dato` no guarda la clase sino el respaldo (DOCUMENTADO, ESTIMACION, PENDIENTE). En la wiki eso se llama «respaldo».

## Estructura de la wiki

```text
wiki/
  index.md                 catálogo: una línea por página, y la tabla de contradicciones
  log.md                   registro cronológico; sólo se agregan entradas al final
  objetivos.md             mapa objetivo -> fuente -> indicador -> página -> decisión
  fuentes/F0N-<tema>.md    una página por fuente
  indicadores/KPI-N-<tema>.md   una página por criterio de éxito de la HU-33
  sintesis/O-N-<tema>.md   una página por objetivo
  consultas/               respuestas a preguntas (etapa 2 en adelante)
  revisiones/              revisiones de salud (etapa 3 en adelante)
```

Nombres de archivo en minúsculas, con guiones, sin tildes ni espacios, salvo el prefijo en mayúsculas (`F02-`, `KPI-1-`, `O-3-`).

## Formato de cada página

Bloque de metadatos YAML al principio:

```yaml
---
tipo: fuente | indicador | sintesis | consulta | revision | indice | log | mapa
fuentes: [F02, F03]
fecha_datos: 2026-09-14        # corte de los datos que usa la página
clase_datos: [FICTICIO, MIXTO] # si usa datos
estado: borrador | revisado | pendiente
actualizado: 2026-11-03
---
```

Las conclusiones que afectan una decisión de compra quedan en `estado: borrador` hasta que una persona del equipo las revise.

## Etiquetas y citas

Cada afirmación relevante lleva una etiqueta y una cita.

| Etiqueta | Cuándo |
|---|---|
| [OBSERVADO] | Lo dice un archivo de `fuentes/` |
| [CALCULADO] | Un número que sale de un archivo, con el cálculo o el comando que lo reproduce |
| [INFERENCIA] | Una conclusión propia a partir de lo observado |
| [SUPUESTO] | Algo que se da por cierto sin evidencia |
| [ESPERADO] | Una meta o resultado esperado |

La cita es un enlace relativo al archivo de `fuentes/` más la fila, columna o sección. Desde una página de `wiki/fuentes/`, `wiki/indicadores/` o `wiki/sintesis/` el prefijo es `../../fuentes/`; desde `wiki/index.md` u `wiki/objetivos.md` es `../fuentes/`. Las rutas con espacios se escriben con `%20`. Ejemplo:

    [F05](../../fuentes/F05_costos_importacion_HU31/hu31_costos_importacion.csv), columna tipo_dato

Todo número tiene que salir de un archivo de `fuentes/` o de un cálculo que se pueda repetir con un comando desde la raíz del repositorio. Si no se puede calcular, se escribe que falta.

## Indicadores

Cada página de `wiki/indicadores/` tiene: fórmula, unidad, granularidad, período, filtros, fuente, meta, línea base con su fecha de medición, valor recalculado a la fecha de la wiki si cambia, ambigüedades de la definición y el comando que reproduce el valor.

## Cuándo actualizar en lugar de crear

- Antes de crear una página, busca en `wiki/` (por nombre de archivo y por el tema en `index.md`). Si ya existe una sobre lo mismo, actualízala.
- Al actualizar, cambia `actualizado` y, si cambia una conclusión, deja la anterior tachada o explicada en una sección «Cambios», con la fecha y la fuente que la motivó.
- Toda página nueva se agrega a `index.md` en la misma pasada. Una página que no está en el índice no existe.

## Contradicciones

- Cuando dos fuentes no coinciden, la página afectada tiene una sección «Contradicciones» con las dos citas, y la contradicción va también a la tabla de `index.md` con un código `C-NN`.
- Se explica cuál prevalece y por qué, o se marca pendiente con lo que haría falta para resolverla. No se elige una en silencio.
- Regla general: el archivo de origen prevalece sobre un resumen (F06 resume a las demás, así lo dice el manifiesto); el criterio aprobado (F03, `CRITERIOS_APROBADOS.md`) prevalece sobre el borrador; para la clase de un conjunto prevalece F02.

## Privacidad

- No copies filas completas de datos a la wiki. Usa conteos y agregados.
- No incluyas nombres de personas fuera del equipo ni datos de contacto. Los códigos de repuesto y de proveedor son ficticios y pueden citarse.

## Registro

Cada etapa agrega una entrada al final de `wiki/log.md` con fecha, etapa, fuentes leídas, páginas creadas y modificadas, y pendientes. Las entradas anteriores no se editan.

## Antes de entregar

1. `git status --short` muestra cambios sólo en `wiki/` y `AGENTS.md`.
2. `python3 src/u4-t1/manifiesto.py` no reporta cambios en las fuentes.
3. Todos los enlaces relativos de la wiki apuntan a archivos que existen y toda página está en `index.md`.
4. Cada número tiene su cita o su comando.
5. `log.md` tiene la entrada de la etapa.
