Terminé la etapa 4. F07 tiene su página, y las páginas que dependen de ella quedaron actualizadas. Ningún valor de indicador cambia: KPI-1 sigue sin poder medirse, KPI-2 está en 40 % y KPI-3 en 50 días. Lo que cambia es qué falta para O1 y O3. `salud.py` da 0 hallazgos en todos los controles, `manifiesto.py` da 17 de 17 copias intactas, y `git status` sólo muestra cambios en `wiki/` y `AGENTS.md` (la carpeta `docs/u4-t1/evidencia/corridas/04/` ya estaba sin seguimiento antes de empezar). No hice commits.

## 1. Archivos

- **Creado:** `wiki/fuentes/F07-datos-simulados-hu34.md`. Su sección «Cambios de esta ingesta» trae una tabla, página por página, de lo que cambió, los enlaces nuevos y si cambia alguna conclusión.
- **Modificados:** `AGENTS.md`, `wiki/index.md`, `objetivos.md`, `log.md`, `F01-pregunta-enfocada.md`, `F02-registro-fuentes-hu02.md`, `F06-portada-repositorio.md`, `KPI-1-mejora-mae-pronostico.md`, `KPI-3-vigencia-datos.md`, `O-1-cuanto-se-vendera.md` y `O-3-datos-al-dia.md`. Cada página tiene su entrada en «Cambios».
- **Sin tocar:** Q-01 y R-01, porque ya están revisadas. Lo que les afecta quedó como pendiente en el log.

## 2. Qué cambia

- **KPI-3, la ambigüedad del conjunto de movimientos:** F07 la acota, pero no la resuelve. La página compara ahora cinco candidatos, todos con datos FICTICIOS, con su fecha y su valor al 3-nov-2026:

  | Candidato | Días | ¿Cumple la meta de 30? |
  |---|---|---|
  | Movimientos de la HU-17 y la HU-30 (los que usa F03) | 50 | No |
  | Ventas de la HU-34 | 10 | Sí, hasta el 2026-11-23 |
  | Inventario de la HU-34 | 10 | Sí, hasta el 2026-11-23 |
  | Compras recibidas de la HU-34 | 11 | Sí, hasta el 2026-11-22 |
  | Compras pedidas de la HU-34 | 40 | No |

  La fecha de las ventas ahora sale del propio CSV y ya no sólo del registro. La wiki sigue usando la definición de F03.
- **KPI-1 y O1:** el estado sigue en «no medible», pero cambia el motivo. Las ventas de F07 cubren 662 días seguidos de 30 repuestos. Con los 3 últimos meses reservados, cada repuesto tiene al menos 246 días con ventas en el año de entrenamiento. Ya existe entonces un historial de prueba con el largo que pide F03. Lo que falta es correr la comparación de métodos sobre él, y que el equipo acepte usar ese historial, porque F03 nombra el de la HU-30.
- **La respuesta de Q-01 se mantiene:** ninguno de los tres criterios respalda hoy una decisión de compra.

## 3. Errores, contradicciones e incertidumbres

- **C-06 (nueva, pendiente):** F07 dice «No se proporcionaron bases empresariales reales para esta actividad». F06 dice que MULTIPARTES facilitó una muestra de unos 20 registros. Las dos fuentes clasifican los datos como FICTICIO. Para el origen de los datos del proyecto dejé que prevalezca F06, y leí la frase de F07 como limitada a la HU-34.
- **C-02 deja de ser hipotética:** los 662 días alcanzan para el año más 3 meses de F03, pero no para los 12 + 12 meses (unos 730 días) de F04. Si se corriera la herramienta de la HU-07 sobre ese historial, no seleccionaría ningún método.
- **C-01 ampliada:** F07 también escribe «MULTIPARTE».
- **Códigos que no cruzan:** F07 usa códigos como `RP001` y F04 como `REP-0001`. No se pueden unir ni comparar repuesto por repuesto.
- **Lo que no se pudo recalcular:** los CSV de compras e inventario no están en `fuentes/`. Sus cifras se citan de la descripción y no se presentan como recalculadas.
- **Q-01, para quien revisa:** su tabla «Qué falta» dice que no existe un historial de un año más 3 meses. Con F07 existe, como dato FICTICIO.

## 4. Pasos siguientes

1. **Fijar el conjunto de movimientos de KPI-3.**
   - Responsable: Samuel (HU-33).
   - Insumo: la tabla de candidatos de KPI-3.
   - Producto: el nombre del conjunto escrito en `CRITERIOS_APROBADOS.md`.
   - Terminado cuando: KPI-3 queda con un solo valor y la ambigüedad 1 cerrada.
2. **Correr la comparación de pronósticos sobre las ventas de F07 y resolver C-02.**
   - Responsable: Fiorella (HU-07 y HU-36).
   - Insumo: `ventas_simuladas.csv`, con 3 meses reservados, y una regla de selección acordada.
   - Producto: una tabla de MAE por método, incorporada como fuente nueva.
   - Terminado cuando: KPI-1 tiene un valor calculado sobre datos FICTICIOS y C-02 queda resuelta.
3. **Aclarar C-06.**
   - Responsable: Fiorella (HU-34).
   - Insumo: F06 y la frase de F07.
   - Producto: la redacción de la HU-34 corregida, o una nota que explique de dónde partió la simulación.
   - Terminado cuando: C-06 queda resuelta en el índice.

Todas las páginas tocadas quedan en `revision: borrador` hasta la revisión humana.