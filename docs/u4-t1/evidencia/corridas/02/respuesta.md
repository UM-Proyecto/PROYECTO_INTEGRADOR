Ninguno de los tres criterios de la HU-33 respalda hoy una decisión de compra. La respuesta está en `wiki/consultas/Q-01-criterios-hu33-al-3-nov.md`, en borrador hasta la revisión humana. `salud.py` da 0 hallazgos en 16 páginas, `manifiesto.py` da 14 de 14 copias intactas, y no hice commits.

## 1. Archivos

- **Creado:** `wiki/consultas/Q-01-criterios-hu33-al-3-nov.md`.
- **Modificados:**
  - `wiki/index.md`: la consulta queda en la sección Consultas.
  - `wiki/objetivos.md`: enlace a Q-01 en «Lectura conjunta».
  - `wiki/log.md`: entrada de la etapa 2.
- `git status` muestra cambios sólo en `wiki/`. La carpeta `docs/u4-t1/evidencia/corridas/02/` ya estaba sin seguimiento antes de esta corrida; no la toqué.

## 2. Respuesta a la pregunta

Volví a calcular todas las cifras desde `fuentes/`, y coinciden con las páginas de cada indicador.

| Criterio | Meta | Valor al 3-nov-2026 | Estado | Clase de datos |
|---|---|---|---|---|
| KPI-1, mejora del error del pronóstico (MAE) | ≥ 15 % | Ningún método elegido: las 30 combinaciones dicen SIN_SELECCION_FIABLE y la evaluación cubre 5 días | No medible | FICTICIO |
| KPI-2, costo con respaldo | ≥ 80 % | 6 de 15 componentes = 40 % | No cumple, faltan 6 componentes | MIXTO, con valores PUBLICOS |
| KPI-3, vigencia de los datos | ≤ 30 días | 3-nov − 14-sep = 50 días | No cumple, 20 días de más | FICTICIO |

Lo que falta para cada uno:
- **KPI-1:** un historial de al menos un año más 3 meses reservados.
- **KPI-2:** facturas para los 4 componentes pendientes y además 2 estimaciones convertidas en documento.
- **KPI-3:** una carga de movimientos con corte al 4-oct-2026 o después.

Lo que tienen en común es que falta información propia de MULTIPARTES. Los valores de KPI-1 y KPI-3 salen de datos de prueba: muestran que el cálculo funciona, no describen a la empresa.

## 3. Contradicciones e incertidumbres

- **C-02 sigue pendiente.** F03 pide un año más 3 meses reservados; F04 exige 12 meses más 12 para elegir un método.
- **La HU-36 no alcanza.** Sus 284 días no están en `fuentes/`, y aunque llegaran quedan por debajo de lo que pide F03.
- **KPI-3 depende del conjunto elegido.** Con `ventas_simuladas` serían 10 días y cumpliría la meta. La consulta sigue a F03, que mide los movimientos al 14-sep.
- **Qué cuenta como respaldo en KPI-2.** Si las 5 estimaciones del INE contaran como documentadas, el valor sería 11 de 15 = 73,3 %, que tampoco cumple.
- **Qué cuenta como componente en KPI-2.** Las 5 cotizaciones documentadas son alternativas de transporte, no partes de un mismo pedido que se sumen.
- **Supuestos que usé:** la fecha de la decisión es el 3-nov-2026, porque no hay ninguna decisión fechada en las fuentes, y el MAE de KPI-1 se promedia entre repuestos.
- **INE sin origen:** su archivo y la URL de descarga no están en `fuentes/`.

## 4. Pasos siguientes

1. **Resolver C-02 y fijar las dos definiciones abiertas** (el conjunto de movimientos de KPI-3 y cómo se agrega KPI-1).
   - Responsable: Samuel (HU-33), con Fiorella (HU-07).
   - Insumo: F03, F04 y las ambigüedades anotadas en KPI-1 y KPI-3.
   - Producto: un criterio aprobado corregido, como fuente nueva F03b.
   - Terminado cuando la wiki quite el «pendiente» de C-02 y KPI-3 nombre el conjunto por su identificador.
2. **Juntar documentos para los 4 componentes pendientes del costo.**
   - Responsable: Samuel, junto con el encargado de compras de MULTIPARTES.
   - Insumo: facturas de seguro, nacionalización, comisiones y flete terrestre.
   - Producto: una tabla F05b.
   - Terminado cuando KPI-2, recalculado, llegue a 12 o más de 15.
3. **Cargar movimientos al día y subir la HU-36.**
   - Responsable: Sabrina (movimientos) y Fiorella (HU-36).
   - Insumo: movimientos con corte al 4-oct-2026 o después y el resultado de la HU-36.
   - Producto: un registro F02 actualizado y una F07.
   - Terminado cuando KPI-3 dé 30 días o menos y la F07 quede ingerida en la etapa 4.