# Crear gráficos para visualizar los resultados de los análisis anteriores. Puedes usar Matplotlib para crear gráficos de barras, gráficos circulares y otros tipos de visualización.
import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos de los archivos CSV

# Gráfico de barras para el envío promedio
envio_promedio = pd.read_csv("./data/envio_promedio.csv")
# Mostrar el gráfico de barras para el envío promedio
plt.bar(envio_promedio["Tienda"], envio_promedio["Envío promedio"])
plt.title("Envío Promedio por Tienda")  # Título del gráfico
plt.xlabel("Tienda")  # Etiqueta del eje x
plt.ylabel("Envío Promedio")  # Etiqueta del eje y
plt.xticks(rotation=45)  # Rotar las etiquetas de las tiendas
plt.tight_layout()  # Ajustar el layout del gráfico
for i in range(len(envio_promedio)):
    plt.text(i, envio_promedio["Envío promedio"].iloc[i] / 2, envio_promedio["Envío promedio"].iloc[i], ha='center', va='center', rotation=90)
plt.savefig("./img/envio_promedio.png")
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de barras para el método de pago más utilizado
metodo_pago = pd.read_csv("./data/metodo_pago.csv")
# Mostrar el gráfico de barras para el método de pago más utilizado
plt.bar(metodo_pago["Tienda"], metodo_pago["Cantidad"])
plt.title("Método de Pago Más Utilizado por Tienda")  # Título del gráfico
for i in range(len(metodo_pago)):
    plt.text(i, metodo_pago["Cantidad"].iloc[i] / 2, metodo_pago["Método de pago"].iloc[i], ha='center', va='center', rotation=90)
plt.xlabel("Tienda")  # Etiqueta del eje x
plt.ylabel("Cantidad")  # Etiqueta del eje y
plt.xticks(rotation=45)  # Rotar las etiquetas de las tiendas
plt.tight_layout()  # Ajustar el layout del gráfico
plt.savefig("./img/metodo_pago.png")
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de barras para la calificación promedio
calificacion_promedio = pd.read_csv("./data/calificacion_promedio.csv")
# Mostrar el gráfico de barras para la calificación promedio
plt.bar(calificacion_promedio["Tienda"], calificacion_promedio["Calificación promedio"])
plt.title("Calificación Promedio por Tienda")  # Título del gráfico
plt.xlabel("Tienda")  # Etiqueta del eje x
plt.ylabel("Calificación Promedio")  # Etiqueta del eje y
plt.xticks(rotation=45)  # Rotar las etiquetas de las tiendas
plt.tight_layout()  # Ajustar el layout del gráfico
for i in range(len(calificacion_promedio)):
    plt.text(i, calificacion_promedio["Calificación promedio"].iloc[i] / 2, calificacion_promedio["Calificación promedio"].iloc[i], ha='center', va='center', rotation=90)  
plt.savefig("./img/calificacion_promedio.png")
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de barras para los productos más vendidos
productos_mas_vendidos = pd.read_csv("./data/productos_mas_vendidos_graficos.csv")
# Sumar los productos más vendidos por producto valores únicos
productos_mas_vendidos_agrupados = productos_mas_vendidos.groupby("Producto")["Cantidad"].sum()

# Crear gráfico de pastel para los productos más vendidos
plt.figure(figsize=(10, 10))  # Ajustar el tamaño de la figura para que sea más grande y legible
plt.pie(productos_mas_vendidos_agrupados, 
        labels=productos_mas_vendidos_agrupados.index, 
        autopct='%1.1f%%', 
        startangle=140,  # Iniciar el gráfico en un ángulo específico para mejor visualización
        labeldistance=1.1,  # Ajustar la distancia de las etiquetas desde el centro
        pctdistance=0.85)  # Ajustar la distancia del porcentaje desde el centro

# Agregar un círculo en el centro para hacer un gráfico de donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')  # Círculo blanco en el centro
fig = plt.gcf()  # Obtener la figura actual
fig.gca().add_artist(centre_circle)  # Añadir el círculo al gráfico

# Agregar título al gráfico
plt.title("Distribución de Productos Más Vendidos", fontsize=16)  # Aumentar el tamaño de la fuente del título

# Ajustar el aspecto del gráfico
plt.axis('equal')  # Asegurarse de que el gráfico sea un círculo

# Guardar el gráfico como imagen
plt.savefig("./img/productos_mas_vendidos.png", bbox_inches='tight')  # Ajustar el recuadro para que no se corte
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de barras para los productos menos vendidos
productos_menos_vendidos = pd.read_csv("./data/productos_menos_vendidos_graficos.csv")
# sumar los productos menos vendidos por producto valores unicos
productos_menos_vendidos_agrupados = productos_menos_vendidos.groupby("Producto")["Cantidad"].sum()


# Crear gráfico de pastel para los productos menos vendidos
plt.figure(figsize=(10, 10))  # Ajustar el tamaño de la figura para que sea más grande y legible
plt.pie(productos_menos_vendidos_agrupados, 
        labels=productos_menos_vendidos_agrupados.index, 
        autopct='%1.1f%%', 
        startangle=140,  # Iniciar el gráfico en un ángulo específico para mejor visualización
        labeldistance=1.1,  # Ajustar la distancia de las etiquetas desde el centro
        pctdistance=0.85)  # Ajustar la distancia del porcentaje desde el centro

# Agregar un círculo en el centro para hacer un gráfico de donut
centre_circle = plt.Circle((0, 0), 0.70, fc='white')  # Círculo blanco en el centro
fig = plt.gcf()  # Obtener la figura actual
fig.gca().add_artist(centre_circle)  # Añadir el círculo al gráfico

# Agregar título al gráfico
plt.title("Distribución de Productos Menos Vendidos", fontsize=16)  # Aumentar el tamaño de la fuente del título

# Ajustar el aspecto del gráfico
plt.axis('equal')  # Asegurarse de que el gráfico sea un círculo

# Guardar el gráfico como imagen
plt.savefig("./img/productos_menos_vendidos.png", bbox_inches='tight')  # Ajustar el recuadro para que no se corte
plt.close()  # Cerrar la figura para liberar memoria

# Gráfico de barras para la facturación por tienda
facturacion_tienda = pd.read_csv("./data/facturacion.csv")

# Limpiar la columna 'Total' para convertirla a numérico
facturacion_tienda["Total"] = facturacion_tienda["Total"].replace({'\\$': '', ',': ''}, regex=True).astype(float)

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))  # Ajustar el tamaño de la figura
plt.bar(facturacion_tienda["Tienda"], facturacion_tienda["Total"], color='skyblue')  # Color de las barras

# Configurar el título y las etiquetas de los ejes
plt.title("Facturación por Tienda", fontsize=16)  # Título del gráfico
plt.xlabel("Tienda", fontsize=14)  # Etiqueta del eje x
plt.ylabel("Facturación", fontsize=14)  # Etiqueta del eje y

# Rotar las etiquetas del eje x para mejor legibilidad
plt.xticks(rotation=45, ha='right')  # Rotar las etiquetas de las tiendas

# Ajustar el layout del gráfico
plt.tight_layout()  # Ajustar el layout para que no se superpongan elementos

# Agregar etiquetas sobre las barras
for i in range(len(facturacion_tienda)):
    plt.text(i, facturacion_tienda["Total"].iloc[i] + 0.05,  # Ajustar la posición vertical
             f'{facturacion_tienda["Total"].iloc[i]:,.0f}',  # Formato de número
             ha='center', va='bottom', fontsize=10)

# Guardar el gráfico como imagen
plt.savefig("./img/facturacion.png", bbox_inches='tight')  # Ajustar el recuadro para que no se corte
plt.close()  # Cerrar la figura para liberar memoria

if __name__ == "__main__":
    print("Calculando gráficos...")
   
