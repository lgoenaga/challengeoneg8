import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Calcular el método de pago más utilizado en cada tienda y su cantidad
metodo_pago_tienda = tienda["Método de pago"].value_counts()
metodo_pago_tienda2 = tienda2["Método de pago"].value_counts()
metodo_pago_tienda3 = tienda3["Método de pago"].value_counts()
metodo_pago_tienda4 = tienda4["Método de pago"].value_counts()

# Obtener el método más utilizado y su cantidad
metodo_pago_mas_usado = metodo_pago_tienda.idxmax()
cantidad_mas_usado = metodo_pago_tienda.max()

metodo_pago_mas_usado2 = metodo_pago_tienda2.idxmax()
cantidad_mas_usado2 = metodo_pago_tienda2.max()

metodo_pago_mas_usado3 = metodo_pago_tienda3.idxmax()
cantidad_mas_usado3 = metodo_pago_tienda3.max()

metodo_pago_mas_usado4 = metodo_pago_tienda4.idxmax()
cantidad_mas_usado4 = metodo_pago_tienda4.max()

# Crear un diccionario con los métodos de pago más utilizados en cada tienda y su cantidad
dic_metodo_pago = {
    "Tienda 1": (metodo_pago_mas_usado, cantidad_mas_usado),
    "Tienda 2": (metodo_pago_mas_usado2, cantidad_mas_usado2),
    "Tienda 3": (metodo_pago_mas_usado3, cantidad_mas_usado3),
    "Tienda 4": (metodo_pago_mas_usado4, cantidad_mas_usado4)
}

# Crear el DataFrame con las columnas "Tienda", "Método de pago" y "Cantidad"
df_metodo_pago = pd.DataFrame(dic_metodo_pago).T.reset_index()
df_metodo_pago.columns = ["Tienda", "Método de pago", "Cantidad"]

# Guardar el DataFrame en un archivo CSV
df_metodo_pago.to_csv("./data/metodo_pago.csv", index=False)

if __name__ == "__main__":
    print("Calculando método de pago...")
   
