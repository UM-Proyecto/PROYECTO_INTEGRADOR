# Cómo reproducir las verificaciones de la U4-T1

Todo se corre desde la raíz del repositorio con Python 3.10 o superior y sólo la biblioteca estándar. Cada script sale con código 0 si todo coincide y con 1 si encuentra un problema, así que se puede encadenar con `&&`.

## 1. Las fuentes no cambiaron

```bash
python3 src/u4-t1/manifiesto.py
```

Recalcula el SHA-256 de cada archivo de `fuentes/` y lo compara con `fuentes/MANIFIESTO.csv`. Reporta las copias que cambiaron, las que faltan y los archivos que sobran. Para comprobar que las copias son idénticas al repositorio de origen, se clona `UM-Proyecto/MINERIA_DATOS`, se hace `git checkout c27757a` y se compara el `sha256sum` de cada `ruta_original` del manifiesto con la columna `sha256`.

## 2. Las cifras de la wiki

```bash
python3 src/u4-t1/verificar.py --csv data/processed/u4-t1/verificaciones.csv
```

Recalcula desde los archivos de `fuentes/` cada cifra que la wiki afirma y la compara con el valor escrito. V1 a V5 son las cifras base de los tres indicadores y del registro de fuentes; Q1 a Q3 son las tres afirmaciones de la consulta Q-01 que se verificaron en la revisión 02, y Q1b es la corrección que salió de esa verificación. A partir de la segunda ingesta se suman las verificaciones I2-N. Cada fila del CSV de salida trae la afirmación, la fuente, el valor recalculado, el afirmado y el resultado.

Además, cada página de indicador de la wiki termina con una sección «Cómo recalcular» que trae el comando de una línea que reproduce su valor.

## 3. La salud de la wiki

```bash
python3 src/u4-t1/salud.py --json data/processed/u4-t1/salud.json
```

Comprueba enlaces Markdown y wikilinks rotos (incluidos los que apuntan a un encabezado que no existe), páginas huérfanas o fuera del índice, metadatos incompletos, indicadores sin alguno de sus campos de definición, cifras sin etiqueta, afirmaciones observadas o calculadas sin cita, la frase prohibida sobre los datos de la empresa, y títulos o nombres de archivo duplicados. Las contradicciones, la vigencia de los datos y la ambigüedad de los indicadores no se pueden juzgar con un script; esas las revisa el agente en la etapa 3 y quedan en `wiki/revisiones/`.

## 4. Las pruebas

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

`test_manifiesto.py` corre el manifiesto. `test_salud.py` arma en un directorio temporal una wiki sana, que tiene que salir con 0 hallazgos, y otra con una falla de cada tipo, que tiene que detectarlas todas. Así se comprueba que el control no da cero por estar roto.

## 5. Repetir una corrida del agente

```bash
src/u4-t1/correr_agente.sh <nn> <etapa> ["texto extra"]
```

Necesita Claude Code instalado y una cuenta con sesión iniciada. El script arma el prompt (`docs/u4-t1/prompts/prompt_mejorado.md` más la línea `ETAPA:`) y corre `claude -p` con el modelo Opus y un directorio de configuración aislado, sin instrucciones personales, memoria, hooks ni servidores MCP. Le permite leer y editar archivos y correr `python3` y comandos de lectura, y le prohíbe hacer commits y usar la red. Guarda el prompt, la transcripción completa (`transcripcion.jsonl`), la respuesta final y el `git status` del final en `docs/u4-t1/evidencia/corridas/<nn>/`. Un modelo de lenguaje no responde dos veces igual, así que una corrida repetida no va a dar el mismo texto; lo que se puede repetir son los controles de los puntos 1 a 4 sobre su resultado.

## 6. Ver qué propuso la IA y qué se corrigió

Cada corrida tiene dos commits: uno con la propuesta del agente tal como quedó, cuyo mensaje empieza con «Corrida NN», y otro con la revisión humana, que empieza con «Revisión NN».

```bash
git log --oneline
git diff <commit de la corrida> <commit de la revisión> -- wiki/ AGENTS.md
```

Las notas de cada revisión, con qué se comprobó y qué se cambió, están en `docs/u4-t1/evidencia/revisiones/`.
