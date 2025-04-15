import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Crear un diccionario para almacenar los productos más vendidos
productos_mas_vendidos = {
    "Tienda 1": tienda["Producto"].value_counts().nlargest(10),
    "Tienda 2": tienda2["Producto"].value_counts().nlargest(10),
    "Tienda 3": tienda3["Producto"].value_counts().nlargest(10),
    "Tienda 4": tienda4["Producto"].value_counts().nlargest(10),
}

# Crear un diccionario para almacenar los productos menos vendidos
productos_menos_vendidos = {
    "Tienda 1": tienda["Producto"].value_counts().tail(10),
    "Tienda 2": tienda2["Producto"].value_counts().tail(10),
    "Tienda 3": tienda3["Producto"].value_counts().tail(10),
    "Tienda 4": tienda4["Producto"].value_counts().tail(10),
}

# Función para crear un DataFrame a partir de un diccionario de productos
def crear_dataframe(productos_dict):
    data = [
        [tienda, producto, cantidad]
        for tienda, productos in productos_dict.items()
        for producto, cantidad in productos.items()
    ]
    return pd.DataFrame(data, columns=["Tienda", "Producto", "Cantidad"])

# Crear DataFrames
productos_mas_vendidos_df = crear_dataframe(productos_mas_vendidos)
productos_menos_vendidos_df = crear_dataframe(productos_menos_vendidos)

# Guardar los DataFrames en archivos CSV
productos_mas_vendidos_df.to_csv("./data/productos_mas_vendidos_graficos.csv", index=False, header=True)
productos_menos_vendidos_df.to_csv("./data/productos_menos_vendidos_graficos.csv", index=False, header=True)

# Función para guardar los productos en un archivo CSV con título
def save_with_title(productos_dict, title_prefix, filename):
    with open(filename, "w") as f:
        for tienda, productos in productos_dict.items():
            f.write(f"{title_prefix} - {tienda}\n")  # Escribir el título de la tienda
            df = pd.DataFrame(productos).reset_index()
            df.columns = ["Producto", "Cantidad"]  # Renombrar columnas
            df.to_csv(f, index=False, header=True)  # Escribir el DataFrame
            f.write("\n")  # Añadir una línea en blanco entre tiendas

# Guardar los productos más vendidos
save_with_title(productos_mas_vendidos, "Productos Más Vendidos", "./data/productos_mas_vendidos.csv")

# Guardar los productos menos vendidos
save_with_title(productos_menos_vendidos, "Productos Menos Vendidos", "./data/productos_menos_vendidos.csv")

# Leer los datos de los productos más vendidos
productos_mas_vendidos_sin_titulos = pd.read_csv("./data/productos_mas_vendidos.csv", skiprows=1)

if __name__ == "__main__":
    print("Calculando productos más y menos vendidos...")