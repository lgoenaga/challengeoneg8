import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Calcular el envío promedio por tienda
envio_promedio = tienda["Costo de envío"].mean()
envio_promedio2 = tienda2["Costo de envío"].mean()
envio_promedio3 = tienda3["Costo de envío"].mean()
envio_promedio4 = tienda4["Costo de envío"].mean()

# Crear un diccionario con las calificaciones formateadas a 2 decimales
dic_tiendas = {
    "Tienda 1": f"{envio_promedio:.2f}",
    "Tienda 2": f"{envio_promedio2:.2f}",
    "Tienda 3": f"{envio_promedio3:.2f}",
    "Tienda 4": f"{envio_promedio4:.2f}"
}

print(dic_tiendas)

# Crear una lista de tuplas con el número de tienda y el envío promedio
data = [(tienda, envio_promedio) for tienda, envio_promedio in dic_tiendas.items()]

# Crear el DataFrame con las columnas "Tienda" y "Envío promedio"
df_tiendas = pd.DataFrame(data, columns=["Tienda", "Envío promedio"])

# Guardar el DataFrame en un archivo CSV
df_tiendas.to_csv("./data/envio_promedio.csv", index=False)


if __name__ == "__main__":
    print("Calculando envío promedio...")
   
