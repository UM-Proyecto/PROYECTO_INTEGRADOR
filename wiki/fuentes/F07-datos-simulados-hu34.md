---
tipo: fuente
subtipo: fuente
fuentes: [F07, F02, F04, F06]
fecha: 2026-10-24
clase_datos: [FICTICIO]
estado: observado
revision: revisado
actualizado: 2026-11-03
tags: [fuente, ficticio]
---

# F07. Datos simulados de la HU-34: descripción, ventas diarias y guía de limpieza

**Archivos:** [`HU34_Descripcion_Datos_MULTIPARTE.md`](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md) (descripción de los tres conjuntos simulados: ventas, compras e inventario), [`ventas_simuladas.csv`](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv) (ventas diarias por repuesto) y [`Guia_Limpieza.md`](../../fuentes/F07_datos_simulados_HU34/Guia_Limpieza.md) (pasos del script de limpieza). **Historia:** HU-34, SCRUM-45 y SCRUM-50, Fiorella Sandoval ([F06](../../fuentes/F06_portada_repositorio/README.md), fila HU-34). **Incorporada:** 3-nov-2026, segunda ingesta ([manifiesto](../../fuentes/MANIFIESTO.md), fila F07).

> Todo F07 es FICTICIO: datos de prueba generados por el equipo. Ninguna cifra de esta página describe las ventas, las compras ni el inventario de MULTIPARTES; sirven para probar métodos. La propia fuente lo dice: los datos «no garantizan precisión ni representan evidencia sobre la empresa» ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Naturaleza y alcance»).

## Qué dice

- [OBSERVADO] Describe tres conjuntos FICTICIOS con más de 3.000 filas cada uno: ventas (19.860 filas, 6 columnas, un repuesto por día con ceros incluidos, 2025-01-01 a 2026-10-24), compras (3.600 filas, 10 columnas, una línea de pedido recibida, pedidos de 2025-01-01 a 2026-09-24) e inventario (19.860 filas, 7 columnas, un repuesto por día y almacén, 2025-01-01 a 2026-10-24) ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Inventario de fuentes»).
- [OBSERVADO] Las compras se reciben del 2025-01-06 al 2026-10-23 ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: compras», rango de `fecha_recepcion`). El inventario trae `entradas` (unidades recibidas de compras) y `salidas` (unidades vendidas) por día, y la fuente verifica que las salidas igualan a las ventas y las entradas a las compras recibidas ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: inventario» y «Construcción y verificación»).
- [OBSERVADO] Faltantes declarados, introducidos a propósito: precio e ingreso en las mismas 199 filas de ventas (1,00 %), proveedor en 72 compras (2,00 %), flete en 108 compras (3,00 %) y almacén en 99 filas de inventario (0,50 %) ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), diccionarios de cada conjunto y «Calidad y relaciones entre fuentes»).
- [OBSERVADO] Generación con Python estándar y semilla 34, 30 códigos de repuesto y 12 de proveedor; inventario inicial de 100 unidades por repuesto; las ventas diarias están limitadas por el stock disponible ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Construcción y verificación»).
- [OBSERVADO] El tipo de cambio de las compras también es simulado: «no provienen de una cotización oficial» ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Naturaleza y alcance»). El costo de las compras excluye tributos y «no permite calcular un costo de importación completo» ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: compras»).
- [OBSERVADO] La guía completa los precios faltantes con el último precio conocido del mismo repuesto, los fletes faltantes con la mediana global del flete por unidad, y marca cada intervención; los valores completados «son estimaciones académicas» ([F07](../../fuentes/F07_datos_simulados_HU34/Guia_Limpieza.md), secciones 3, 4 y 6). Los archivos limpios que produce el script no están en `fuentes/`.
- [OBSERVADO] La fuente advierte que el número de filas no equivale a una muestra independiente y que la utilidad de los pronósticos «deberá evaluarse con partición temporal y comparación con un modelo base» ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Cumplimiento de HU-34»).

## Verificación contra el archivo de ventas

De los tres conjuntos, sólo el de ventas está en `fuentes/`. Las cifras de compras e inventario quedan como [OBSERVADO] de la descripción y no se pueden recalcular. Comandos en «Cómo recalcular».

- [CALCULADO] `ventas_simuladas.csv` tiene 19.860 filas, 30 repuestos (RP001 a RP030), 662 fechas del 2025-01-01 al 2026-10-24 sin huecos (662 días calendario) y ninguna clave fecha + sku repetida; precio e ingreso están vacíos en las mismas 199 filas y ninguna otra columna tiene vacíos ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columnas `fecha`, `sku`, `precio_unitario_bs` e `ingreso_bs`). Coincide con la descripción.
- [CALCULADO] La huella SHA-256 del archivo es la misma que registra F02 para `ventas_simuladas`, con 19.860 registros y corte 2026-10-24 ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `ventas_simuladas`, columnas `sha256`, `registros` y `fecha_corte_datos`). F07 y F02 hablan del mismo archivo.
- [CALCULADO] De las 19.860 filas, 1.782 tienen cero unidades vendidas (9,0 %). Cada repuesto tiene entre 504 y 657 días con ventas ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `unidades_vendidas`). Sobre datos FICTICIOS, esto prueba que el conjunto sirve para series diarias, no que la empresa venda así.

## Para qué sirve en la wiki

- [[KPI-3-vigencia-datos|KPI-3]]: da un segundo candidato a «datos de movimientos», con fecha verificable en el propio archivo. [CALCULADO] Con las ventas FICTICIAS al 2026-10-24, el indicador daría 10 días al 3-nov-2026 ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `fecha`). No cambia el valor de la wiki, que sigue a F03 (ver [[KPI-3-vigencia-datos#Ambigüedades|ambigüedad 1]]).
- [[KPI-1-mejora-mae-pronostico|KPI-1]]: [CALCULADO] es el primer conjunto en `fuentes/` con el largo que pide F03, un año de entrenamiento más 3 meses reservados: 662 días ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `fecha`; [F03](../../fuentes/F03_criterios_exito_HU33/CRITERIOS_APROBADOS.md), fila 1). Nadie ha corrido todavía la comparación de métodos sobre él, así que KPI-1 sigue sin medirse.
- [[O-2-cuanto-cuesta-traerlo|O-2]]: [INFERENCIA] no aporta respaldo al costo de importación. Sus costos y su tipo de cambio son FICTICIOS y no incluyen tributos, así que no cambian [[KPI-2-costo-con-respaldo|KPI-2]].

## Limitaciones

- [OBSERVADO] Los códigos de repuesto de F07 tienen la forma `RP001` y los de F04 la forma `REP-0001` ([F07](../../fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv), columna `sku`; [F04](../../fuentes/F04_pronosticos_HU07/comparacion_pronosticos.csv), columna `codigo_unico`). [INFERENCIA] Son dos simulaciones distintas: no se pueden unir por repuesto ni comparar repuesto a repuesto. F07 tiene 30 repuestos; el catálogo FICTICIO de la HU-17 tiene 20 registros ([F02](../../fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv), fila `catalogo_repuestos`).
- [OBSERVADO] Las ventas observadas «pueden subestimar la demanda cuando hay faltantes» y el conjunto no permite medir ventas perdidas ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Conjunto: ventas»). Es la misma advertencia de la ambigüedad 4 de [[KPI-1-mejora-mae-pronostico#Ambigüedades|KPI-1]].
- [OBSERVADO] Compras e inventario se describen pero sus CSV no están en `fuentes/`; la guía de limpieza remite a `data/raw/hu-34/` y `data/processed/hu-34/` del repositorio del equipo ([F07](../../fuentes/F07_datos_simulados_HU34/Guia_Limpieza.md), primer párrafo).

## Contradicciones

- **C-06. Origen de los datos.** [OBSERVADO] F07 dice: «No se proporcionaron bases empresariales reales para esta actividad. Se construyeron tres fuentes FICTICIAS para fines académicos» ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Naturaleza y alcance»). F06 dice: «MULTIPARTES facilitó una muestra inicial pequeña, de unos 20 registros. Para poder aplicar y comparar las técnicas, el equipo la amplió con datos de prueba con la misma estructura» ([F06](../../fuentes/F06_portada_repositorio/README.md), «De dónde salen los datos»). [INFERENCIA] Las dos coinciden en la clase (FICTICIO) y en que los datos no describen a la empresa; difieren en lo que dicen sobre la empresa. La frase de F07 se limita a «esta actividad», y la generación con semilla, los 30 repuestos y los códigos `RP001` sugieren que la HU-34 no partió de la muestra de unos 20 registros. **Para describir el origen de los datos del proyecto prevalece F06**, que es la versión del equipo para todo el repositorio y la que fija el manifiesto ([manifiesto](../../fuentes/MANIFIESTO.md), «Cómo se clasifican los datos»). **Pendiente** que la responsable de la HU-34 diga si su simulación usó la muestra y ajuste la redacción. No cambia ninguna cifra.
- **C-01 (ampliada). Nombre de la empresa.** [OBSERVADO] F07 escribe «MULTIPARTE» en el título del archivo y en el texto ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Empresa y propósito»), igual que el objetivo de F01. Prevalece «MULTIPARTES»; ver [[F01-pregunta-enfocada#Contradicciones|F01]].

## Privacidad

[OBSERVADO] F07 no trae datos personales ni precios reales; los repuestos y los proveedores tienen códigos ficticios ([F07](../../fuentes/F07_datos_simulados_HU34/HU34_Descripcion_Datos_MULTIPARTE.md), «Construcción y verificación»). La wiki usa sólo conteos y agregados del CSV.

## Cómo recalcular

Forma del archivo (filas, primera y última fecha, fechas distintas, repuestos, claves repetidas y vacíos por columna):

    python3 -c "import csv,collections as c;r=list(csv.DictReader(open('fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv',encoding='utf-8-sig')));f=[x['fecha'] for x in r];print(len(r),min(f),max(f),len(set(f)),len({x['sku'] for x in r}),len(r)-len({(x['fecha'],x['sku']) for x in r}),{k:sum(x[k]=='' for x in r) for k in r[0]})"

Días con cero ventas, su porcentaje y el mínimo y máximo de días con ventas por repuesto:

    python3 -c "import csv,collections as c;r=list(csv.DictReader(open('fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv',encoding='utf-8-sig')));z=sum(x['unidades_vendidas']=='0' for x in r);d=c.Counter(x['sku'] for x in r if x['unidades_vendidas']!='0');print(z,round(z/len(r)*100,1),min(d.values()),max(d.values()))"

Huella frente al registro de F02:

    python3 -c "import csv,hashlib;h=hashlib.sha256(open('fuentes/F07_datos_simulados_HU34/ventas_simuladas.csv','rb').read()).hexdigest();g=[x for x in csv.DictReader(open('fuentes/F02_registro_fuentes_HU02/registro_actualizaciones.csv',encoding='utf-8')) if x['conjunto']=='ventas_simuladas'][0];print(h==g['sha256'],g['registros'],g['fecha_corte_datos'])"

## Cambios de esta ingesta

Segunda ingesta, 3-nov-2026. Antes de ella la wiki conocía los conjuntos de la HU-34 sólo por su renglón en el registro F02. Lo que cambió, página por página:

| Página | Qué cambió | Enlaces nuevos | ¿Cambia una conclusión? |
|---|---|---|---|
| Esta página (nueva) | Descripción de F07, verificación del CSV de ventas, C-06 | a F01, F02, F06, KPI-1, KPI-2, KPI-3, O-2 | — |
| [[KPI-3-vigencia-datos|KPI-3]] | La ambigüedad 1 pasa de un candidato visto en el registro a cuatro fechas de F07 con su valor: ventas e inventario dan 10 días, recepción de compras 11, pedidos 40. Comando nuevo que lee la fecha en el propio CSV | a F07 | No. El valor sigue en 50 días con la definición de F03 y la ambigüedad sigue pendiente; ahora se sabe que con los datos de la HU-34 se cumpliría hasta el 23-nov-2026 |
| [[KPI-1-mejora-mae-pronostico|KPI-1]] | «Qué falta»: ya hay un historial FICTICIO de 662 días que alcanza el año más 3 meses de F03, y cada repuesto tiene al menos 246 días con ventas en un año de entrenamiento. C-02 se vuelve concreta: con ese historial F03 se podría medir y la regla de F04 (12 + 12 meses) seguiría sin seleccionar | a F07 | Sí, en parte. El estado sigue en «no medible», pero el motivo cambia: ya no falta historial de prueba, falta correr la comparación sobre él y resolver C-02 |
| [[O-1-cuanto-se-vendera|O-1]] | Mismo cambio que KPI-1, y la observación de que las ventas esporádicas de F04 no se repiten en F07 | a F07 | Sí, en parte: «lo que falta es historial» pasa a «lo que falta es la comparación sobre el historial de F07 y la regla de selección» |
| [[O-3-datos-al-dia|O-3]] | Candidatos de F07 en «Qué significa» y «Qué falta» | a F07 | No |
| [[F02-registro-fuentes-hu02|F02]] | Las filas de la HU-34 enlazan a F07; observación de que la huella coincide | a F07 | No |
| [[F06-portada-repositorio|F06]] | C-06 en «Contradicciones»; ya no es cierto que ninguna fuente diga que la empresa no dio datos | a F07 | No |
| [[F01-pregunta-enfocada|F01]] | C-01 incluye a F07 | a F07 | No |
| [[objetivos]] | F07 en el mapa (fuentes de O1 y O3) y en la lectura conjunta | a F07 | No: ninguno de los tres criterios alcanza su meta |
| [[index]] | Línea de F07, C-01 ampliada, C-06 nueva, ambigüedades de KPI-1 y KPI-3 | a F07 | — |
| [[AGENTS]] | Las fuentes vigentes son F01 a F07 | — | — |

[INFERENCIA] Para la pregunta de negocio, la respuesta de [[Q-01-criterios-hu33-al-3-nov|Q-01]] se sostiene: ningún criterio respalda hoy una decisión de compra. Q-01 tiene `revision: revisado` y el agente no la edita. Quedan dos cosas para la persona que revisa: su tabla «Qué falta» dice que el historial de un año más 3 meses no existe, y con F07 existe como dato FICTICIO; además, su vacío 5 (C-02) ya tiene un caso concreto.
