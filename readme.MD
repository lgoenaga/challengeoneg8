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
