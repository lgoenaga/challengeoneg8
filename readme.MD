# CHALLENGE ONE G8
___

Durante este desafío, ayudarás al Sr. Juan a decidir qué tienda de su cadena **Alura Store** debe vender para iniciar un nuevo emprendimiento. Para ello, analizarás datos de ventas, rendimiento y reseñas de las cuatro tiendas de Alura Store. El objetivo es identificar la tienda menos eficiente y presentar una recomendación final basada en los datos.

## Lo que se realizará:

- **Cargar y manipular datos CSV** con la biblioteca **Pandas**.
- **Crear visualizaciones de datos** con la biblioteca **Matplotlib**.
- **Analizar métricas** como ingresos, reseñas y rendimiento de ventas.

## Requisitos:

### Analizar datos de la tienda:

Debes evaluar información como:
- Ingresos
- Categorías más vendidas
- Reseñas de los clientes
- Productos más vendidos
- Envío promedio

### Crear gráficos para visualización:

Decide qué tipos de gráficos utilizar para presentar los resultados de forma clara y visual. Se requiere un mínimo de **tres gráficos diferentes**, que pueden incluir:
- Gráficos de barras
- Gráficos circulares
- Gráficos de dispersión
- Otros tipos de visualización

### Enviar una recomendación:

Después del análisis, redacta un texto explicando a qué tienda debería vender el Sr. Juan y por qué, basándote en los datos presentados.

# INICIO

## Extracción de datos

Los datos de cada tienda están disponibles en archivos CSV y se cargarán utilizando el código base ya proporcionado. El código extrae información de las cuatro tiendas y organiza los datos en DataFrames utilizando la biblioteca Pandas.

**Código base**

## Detalles importantes:

Código base: Ya está listo para extraer y organizar los datos correctamente, recomendamos no modificarlo.

Los datos se almacenan en DataFrames: cada tienda tiene su propio conjunto de datos (store1, store2, store3 y store4), y debes usarlos para los siguientes pasos del desafío.

https://github.com/lgoenaga/challengeoneg8.git

https://github.com/lgoenaga/challengeoneg8/blob/main/documents/AluraStoreLatam.ipynb

** Cargar los datos de las tiendas **
Goolge colab

## Conozca el conjunto de datos

Antes de pasar a análisis detallados, es esencial explorar el conjunto de datos para comprender su estructura y contenido. Este paso le permite identificar patrones, inconsistencias y las columnas más relevantes para los siguientes pasos.

### Estructura de datos:

El conjunto de datos incluye la siguiente información:

- **Producto y Categoría**: Artículos vendidos y sus calificaciones.
- **Precio y Envío**: Valores de venta y costos asociados.
- **Fecha y ubicación de compra**: Información temporal y geográfica.
- **Evaluación de compra**: Comentarios de clientes.
- **Tipo de Pago y Cuotas**: Métodos utilizados por los clientes.
- **Coordenadas Geográficas**: Ubicación de las transacciones.

## Análisis de datos
### Análisis de ingresos
- **Total de ingresos**: Calcular el total de ingresos generados por cada tienda.
- **Promedio de ingresos**: Calcular el ingreso promedio por tienda.

# DESARROLLO

1. **Instalación de bibliotecas**: Asegúrate de tener instaladas las bibliotecas necesarias, como Pandas y Matplotlib.
2. Clonar el repositorio: Clona el repositorio de GitHub que contiene los datos y el código base. Puedes usar el siguiente comando en tu terminal:

```bash
git clone https://github.com/lgoenaga/challengeoneg8.git
```
3. **Carga de datos**: Cargar los datos de las cuatro tiendas utilizando Pandas. Para la carga de datos, puedes usar el siguiente código:
```python
python3 main.py
```
4. **Facturación**: Calcular la facturación total de cada tienda.
```python
python3 facturacion.py
```
5. **Ventas por categoría**: Calcular las ventas por categoría de productos.
```python
python3 ventas_por_categoria.py
```
6. **Calificación promedio de la tienda**: Calcular la calificación promedio de cada tienda.
```python
python3 calificacion_promedio.py
```
7. **Productos más y menos vendidos**: Identificar los 10 productos más y menos vendidos en cada tienda.
```python
python3 productos_mas_menos_vendidos.py
```
8. **Envío promedio por tienda**: Calcular el envío promedio por tienda.
```python
python3 envio_promedio.py
```
9. **Método de pago más utilizado**: Identificar el método de pago más utilizado en cada tienda.
```python
python3 metodo_pago.py
```
10. **Gráficos**: Crear gráficos para visualizar los resultados de los análisis anteriores. Puedes usar Matplotlib para crear gráficos de barras, gráficos circulares y otros tipos de visualización.
```python
python3 graficos.py
```
11. **Recomendación final**: Redactar un texto explicando qué tienda debería vender el Sr. Juan para mejorar sus ingresos y no tener mayores perdidas, basándote en los datos presentados.

## Recomendación Final

Después de analizar los datos de facturación, envío promedio, calificación promedio y ventas de productos más y menos vendidos, se recomienda al Sr. Juan que **evite vender en la Tienda 4**. A continuación se detallan las razones y justificaciones:

1. **Baja Facturación**: 
   - La Tienda 4 tiene la menor facturación, alcanzando **$1,093,693,100.00**. Esto indica que, a pesar de tener un volumen de ventas, no está generando ingresos suficientes en comparación con las otras tiendas. Una menor facturación puede traducirse en menos recursos para reinvertir en el negocio.

2. **Menor Variedad de Productos Populares**: 
   - Aunque la Tienda 4 tiene un costo de envío promedio más bajo (**23,459.46**), lo que podría parecer ventajoso, la falta de productos populares limita las oportunidades de venta. La Tienda 4 no cuenta con productos que atraigan a un gran número de clientes, lo que puede resultar en un menor interés y, por ende, en menos ventas.

3. **Riesgo de Pérdidas**: 
   - La Tienda 4 tiene varios productos menos vendidos, como la **silla de oficina** y el **celular ABXY**. Esto sugiere que hay un riesgo significativo de tener un exceso de inventario en productos que no se venden bien. Mantener productos que no tienen demanda puede resultar en pérdidas financieras y costos adicionales de almacenamiento.

4. **Calificación Promedio**: 
   - La Tienda 4 tiene una calificación promedio de **4.00**, que aunque es aceptable, no es la más alta en comparación con las otras tiendas. Una calificación más baja puede indicar problemas en la satisfacción del cliente, lo que podría afectar la reputación de la tienda y, en consecuencia, las ventas futuras.

5. **Comparación con Otras Tiendas**: 
   - En contraste, las Tiendas 1, 2 y 3 presentan una mejor combinación de alta facturación, productos populares y calificaciones más altas. Por ejemplo, la Tienda 1 tiene la mayor facturación y una buena variedad de productos, lo que la convierte en una opción más atractiva para el Sr. Juan.

**En conclusión**, el Sr. Juan debería considerar vender en las **Tiendas 1, 2 o 3**, que ofrecen mejores oportunidades de venta y satisfacción del cliente. Debería considerar vender la Tienda 4 no solo minimizará el riesgo de pérdidas, sino que también permitirá al Sr. Juan enfocarse en maximizar sus ingresos y mejorar su rentabilidad, la otra opción es cambiar los productos menos vendidos por otros que tengan una mejor aceptación en el mercado.

## Conclusión
Este desafío ha permitido al Sr. Juan tomar decisiones informadas sobre su negocio, basándose en datos concretos y análisis detallados. La combinación de análisis de datos y visualización ha facilitado la identificación de áreas de mejora y oportunidades para maximizar los ingresos.

