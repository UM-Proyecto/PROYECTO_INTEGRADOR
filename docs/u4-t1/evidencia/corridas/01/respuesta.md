Terminé la etapa 1. Las 15 páginas tienen metadatos, ningún enlace interno está roto y todas se enlazan desde `index.md`. Los siete comandos de recálculo que hay en las páginas corren y dan las mismas cifras que la wiki. `manifiesto.py` da 14 de 14 copias intactas, y `git status` sólo muestra `AGENTS.md` y `wiki/` como nuevos. La carpeta `docs/u4-t1/evidencia/corridas/01/` ya estaba sin seguimiento antes de empezar y no la toqué. No hice commits.

## 1. Archivos creados

- `AGENTS.md`
- `wiki/index.md`, `wiki/log.md`, `wiki/objetivos.md`
- `wiki/fuentes/`: `F01-pregunta-enfocada.md`, `F02-registro-fuentes-hu02.md`, `F03-criterios-exito-hu33.md`, `F04-pronosticos-hu07.md`, `F05-costos-importacion-hu31.md`, `F06-portada-repositorio.md`
- `wiki/indicadores/`: `KPI-1-mejora-mae-pronostico.md`, `KPI-2-costo-con-respaldo.md`, `KPI-3-vigencia-datos.md`
- `wiki/sintesis/`: `O-1-cuanto-se-vendera.md`, `O-2-cuanto-cuesta-traerlo.md`, `O-3-datos-al-dia.md`

No modifiqué ningún archivo existente.

**Valores al 3-nov-2026**, todos en estado borrador:

| Indicador | Meta | Valor | Estado |
|---|---|---|---|
| KPI-1, pronóstico | 15 % menos de error | No medible | Las 30 filas de F04 dicen `SIN_SELECCION_FIABLE`. Con los datos FICTICIOS el MAE medio es 0,14, 0,14 y 0,32: ningún método mejora al «último periodo» |
| KPI-2, costo con respaldo | 80 % o más | 6 de 15 = 40 % | No cumple. Faltan 6 componentes documentados |
| KPI-3, vigencia | 30 días o menos | 50 días (eran 42 en la línea base del 26-oct) | No cumple |

## 2. Respuesta a la pregunta

No corresponde: la consulta es la etapa 2.

## 3. Errores, contradicciones e incertidumbres

**Contradicciones entre fuentes** (están en `index.md` y en la página afectada):
- **C-01:** el objetivo de F01 dice «MULTIPARTE» y la pregunta dice «MULTIPARTES». Dejé «MULTIPARTES» porque parece una errata.
- **C-02:** para el pronóstico, F03 pide un año de historial más 3 meses reservados y F04 pide 12 meses más 12. Prevalece F03, pero queda pendiente que el equipo alinee las dos reglas.
- **C-03:** F06 llama MIXTO a la HU-32, pero F02 registra `tc_series_diaria` como PUBLICO. Queda F02 y la duda pendiente.
- **C-04:** F06 dice que la tabla de costos es MIXTO por las «cotizaciones de proveedor FICTICIAS», pero ninguna de sus 15 filas trae una cotización: 11 tienen respaldo público y 4 están vacías. Mantuve MIXTO, porque la clase la fija F02, y dejé la aclaración pendiente.

**Ambigüedades en los indicadores:**
- **KPI-3 es la más seria.** F03 no dice qué conjunto cuenta como «movimientos». Con `ventas_simuladas` (HU-34, corte al 24-oct) el valor sería de 10 días y cumpliría la meta, así que el resultado depende de una definición, no de los datos.
- **KPI-2:** las 5 cotizaciones son alternativas de transporte, no partes que se suman, y el SCFI es un índice, no un costo. Además, F03 acepta una «publicación» como respaldo, pero las 5 estimaciones del INE no se cuentan como documentadas.
- **KPI-1:** F03 no dice cómo se agregan los repuestos. Además, 7 de 10 repuestos no tienen ventas en la ventana evaluada, así que su MAE de cero no valida ningún método.

**Faltan en `fuentes/`:** el resultado de la HU-36 (284 días), el CSV del INE y `REPORTE_HU07.md`. Además, la línea base de KPI-3 está fechada el 26-oct, pero la única carga de F02 es del 27-oct.

## 4. Pasos siguientes

1. **Fijar las definiciones (KPI-3 y C-02).**
   - **Responsable:** Samuel, dueño de la HU-33.
   - **Insumo:** las secciones de ambigüedades de KPI-1 y KPI-3, y C-02.
   - **Producto:** una nota de aprobación que nombre el conjunto de movimientos y una única regla de historial.
   - **Hecho cuando:** la nota esté copiada como fuente nueva y KPI-3 tenga un solo valor.
2. **Conseguir los 4 componentes PENDIENTE del costo.**
   - **Responsable:** Samuel, dueño de la HU-31, junto con el jefe de compras.
   - **Insumo:** las filas PENDIENTE de F05.
   - **Producto:** facturas de seguro, nacionalización, comisiones y flete terrestre.
   - **Hecho cuando:** la tabla nueva esté en `fuentes/`. Ojo: aun así KPI-2 llegaría a 10 de 15 (66,7 %), y para el 80 % hacen falta 2 documentos más.
3. **Subir el resultado de la HU-36 y conseguir historial real.**
   - **Responsable:** Fiorella, dueña de la HU-07 y la HU-36.
   - **Insumo:** el resultado con 284 días que hoy está comentado en Jira.
   - **Producto:** el CSV en el repositorio, copiado como F0N.
   - **Hecho cuando:** KPI-1 tenga un valor calculable con un año de historial y 3 meses reservados, o la wiki diga con fuente por qué todavía no lo tiene.