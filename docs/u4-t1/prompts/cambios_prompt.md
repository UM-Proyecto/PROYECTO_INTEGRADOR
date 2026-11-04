# Qué cambió del prompt inicial al mejorado, y por qué

Al completar el prompt genérico con los datos del proyecto (`prompt_inicial.md`) quedaron a la vista siete problemas. Cada cambio del prompt mejorado responde a uno.

La pregunta de negocio del prompt inicial era la pregunta enfocada del proyecto copiada tal cual. Es una pregunta de investigación para el semestre y no se puede verificar en una consulta: no dice qué número respondería. La versión mejorada la baja a una pregunta que sí se puede comprobar (qué criterios de la HU-33 respaldan hoy una decisión, con qué valor frente a su meta y qué falta) y dice qué evidencia permite juzgar si la respuesta sirve.

El objetivo único se dividió en tres, uno por cada cosa que una compra necesita saber (cuánto se vende, cuánto cuesta traerlo, si los datos están al día). Así cada objetivo queda atado a un indicador y a una página, que es el mapa que pide la rúbrica, y el agente no tiene que inventar la relación.

«Las fuentes de la carpeta fuentes/» no le decía al agente qué versión estaba leyendo. El prompt mejorado nombra el repositorio, el commit y la fecha de copia, enumera las fuentes con su código y le prohíbe salir de esa carpeta.

El proyecto mezcla datos de prueba y datos públicos, y una frase mal puesta («la empresa no entregó datos») le cambia el sentido al trabajo frente a MULTIPARTES. El prompt mejorado fija el vocabulario del registro de la HU-02 (FICTICIO, PUBLICO, MIXTO), la frase correcta sobre la muestra de unos 20 registros, y la regla de que un resultado sobre datos de prueba se presenta como prueba del método.

El prompt inicial pedía separar hechos, cálculos, inferencias y supuestos, pero no decía cómo. El mejorado define cinco etiquetas con su significado, un formato de cita con fila o columna, un bloque de metadatos por página y una sección fija para las contradicciones.

El genérico pedía hacer todo de una vez. El mejorado separa cuatro etapas y le pide al agente que se detenga al terminar cada una, para que la revisión humana lea y acepte un cambio por vez y el historial de git muestre qué propuso la IA y qué se corrigió. Por la misma razón el agente no hace commits.

Por último, se agregaron criterios de aceptación que se pueden comprobar con un comando (archivos tocados, enlaces, números, campos de cada indicador, marcas de origen y entrada en el registro). Son los que se usan en `docs/u4-t1/evidencia/revisiones/` para aceptar o corregir cada corrida.
