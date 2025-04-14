import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Crear un diccionario para almacenar los productos más vendidos
productos_mas_vendidos = {
    "Tienda 1": tienda["Producto"].value_counts().nlargest(10),  # Obtener los 10 más vendidos
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

# Función para guardar los productos en un archivo CSV
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

if __name__ == "__main__":
    print("Calculando productos más y menos vendidos...")