import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Calcular los totales
total_tienda = tienda["Precio"].sum() + tienda["Costo de envío"].sum()
total_tienda2 = tienda2["Precio"].sum() + tienda2["Costo de envío"].sum()
total_tienda3 = tienda3["Precio"].sum() + tienda3["Costo de envío"].sum()
total_tienda4 = tienda4["Precio"].sum() + tienda4["Costo de envío"].sum()

# Crear una lista de tuplas con el nombre de la tienda y el total
data = [
    ("Tienda 1", total_tienda),
    ("Tienda 2", total_tienda2),
    ("Tienda 3", total_tienda3),
    ("Tienda 4", total_tienda4)
]

# Crear el DataFrame con las columnas "Tienda" y "Total"
df_tiendas = pd.DataFrame(data, columns=["Tienda", "Total"])

# Formatear la columna "Total" a dos decimales con símbolo de dólar
df_tiendas['Total'] = df_tiendas['Total'].apply(lambda x: "${:,.2f}".format(x))

# Guardar el DataFrame en un archivo CSV
df_tiendas.to_csv("./data/facturacion.csv", index=False)

if __name__ == "__main__":
    print("Calculando facturación...")
   
