import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Calcular el método de pago más utilizado en cada tienda
metodo_pago_tienda = tienda["Método de pago"].value_counts()
metodo_pago_tienda2 = tienda2["Método de pago"].value_counts()
metodo_pago_tienda3 = tienda3["Método de pago"].value_counts()
metodo_pago_tienda4 = tienda4["Método de pago"].value_counts()

# Crear un diccionario con los métodos de pago y sus respectivas cantidades
dic_metodo_pago = {
    "Tienda 1": metodo_pago_tienda,
    "Tienda 2": metodo_pago_tienda2,
    "Tienda 3": metodo_pago_tienda3,
    "Tienda 4": metodo_pago_tienda4
}   

print(dic_metodo_pago)

# Crear el DataFrame con las columnas "Tienda" y "Método de pago"
df_metodo_pago = pd.DataFrame(dic_metodo_pago.items(), columns=["Tienda", "Método de pago"])

# Guardar el DataFrame en un archivo CSV
df_metodo_pago.to_csv("./data/metodo_pago.csv", index=False)

if __name__ == "__main__":
    print("Calculando método de pago...")
   
