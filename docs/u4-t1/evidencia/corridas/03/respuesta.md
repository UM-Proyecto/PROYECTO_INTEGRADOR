Terminé la etapa 3. Antes de cambiar nada, `salud.py` ya daba 0, pero leyendo cada página contra `fuentes/` aparecieron 13 problemas que el script no detecta. Corregí diez y dejé tres pendientes. Ningún valor de indicador cambió, y la respuesta de Q-01 sigue igual: ninguno de los tres criterios respalda hoy una compra.

Al final, `salud.py` da 0 en sus once controles sobre 17 páginas y `manifiesto.py` da 14 de 14 copias intactas. Todas las cifras de la wiki se volvieron a calcular desde `fuentes/` y coinciden.

**Ojo: `docs/u4-t1/REPRODUCIR.md` cambió en el working tree y no lo toqué yo.** Se modificó a las 21:25 y además apareció un commit nuevo, `9b3017c`. Parece trabajo de alguien del equipo hecho en paralelo; no lo revertí. Tenlo en cuenta al revisar `git status`, porque el criterio de «nada fuera de `wiki/` y `AGENTS.md`» va a fallar por ese archivo y no por esta corrida.

### (1) Archivos

- **Creado:** `wiki/revisiones/R-01-salud-3-nov.md`
- **Modificados:** `AGENTS.md`, `index.md`, `objetivos.md`, `log.md`, F04, F05, F06, KPI-1, KPI-2, KPI-3, O-1, O-2 y O-3. Cada página modificada tiene una sección «Cambios» con la fecha y el código del hallazgo.

### (3) Errores, contradicciones e incertidumbres

**Corregidos:**
- **H-01:** O-3 pedía un corte de movimientos «posterior al 2026-10-04». Un corte ese mismo día ya da 30 días y cumple la meta.
- **H-03:** C-04 decía que la HU-31 tiene dos conjuntos. F02 le registra tres.
- **H-04:** F02 tiene un conjunto FICTICIO de «seguro y otros costos de importación» con 4 registros que la wiki no mencionaba. Aunque tuviera valores para los 4 componentes pendientes, no sube KPI-2: un dato de prueba no es un documento de respaldo.
- **H-05:** Ningún repuesto cumple la regla de F04 de tener tres días con ventas en entrenamiento (las 30 filas lo dicen). Entonces la falta de un método elegido no se debe sólo a que el historial es corto. Esto también explica el empate en 0,467: esos repuestos no vendieron nada antes, así que los tres métodos pronostican cero.
- **H-06:** F06 resume los criterios con otras palabras que F03. Para KPI-3 importa: F06 habla de «la fecha de los datos», sin decir «de movimientos», lo que deja aún más abierto qué conjunto usar.
- **H-07, H-08:** dos etiquetas estaban mal puestas y once afirmaciones no tenían etiqueta.
- **H-09:** el corte de las referencias de flete figura al 9-oct, pero 5 de los 6 respaldos documentados de KPI-2 son cotizaciones de junio, con 154 días de antigüedad al 3-nov. R-01 tiene una tabla con la antigüedad de cada conjunto.
- **H-12, H-13:** faltaba en `AGENTS.md` la regla de citas para consultas y revisiones, y el índice todavía decía que no había revisiones.

**Pendientes:**
- **C-05, contradicción nueva:** el manifiesto y F06 definen MIXTO como datos públicos combinados con datos de prueba. La tabla de costos está registrada como MIXTO pero no tiene ningún dato de prueba. El motivo que dio la revisión 01 al cerrar C-04 no sale de ninguna fuente. La clase se deja como dice F02 hasta que decida el responsable del conjunto. El valor de KPI-2 no cambia.
- **H-10:** Q-01 está marcada como `revisado` y no la edité. Su aviso inicial todavía dice «queda en borrador», y si se acepta C-05 cambia la columna de clase de datos de KPI-2.
- **H-11:** el campo `fecha` no se usa igual en las páginas que combinan varios cortes. En R-01 propongo usar el corte más antiguo, pero no lo apliqué porque cambia la convención para toda la wiki.

### (4) Siguientes pasos

1. **Resolver C-05.** Responsable: Samuel Castillo. Insumo: F02, fila `costos_importacion`, y la definición del manifiesto. Producto: la clase confirmada o corregida, anotada en F05, KPI-2, O-2 y Q-01. Se termina cuando C-05 dice «resuelta» en el índice y `salud.py` sigue en 0.
2. **Revisar R-01 y actualizar Q-01.** Responsable: quien haga la revisión humana. Insumo: R-01 y la sección «Cambios» de cada página. Producto: el aviso de Q-01 corregido y R-01 marcada como `revisado`. Se termina cuando ninguna página revisada dice «borrador» en su texto.
3. **Fijar las definiciones de KPI-1 y KPI-3.** Responsables: el equipo, con Fiorella Sandoval para KPI-1. Insumo: las ambigüedades de KPI-1 y KPI-3, C-02 y la regla de tres días con ventas de F04. Producto: una F03 actualizada que diga cómo se agregan los repuestos y qué conjunto de movimientos se usa. Se termina cuando esa fuente llegue como F07 y se ingiera en la etapa 4.

Todo queda en borrador hasta la revisión humana. No hice commits.