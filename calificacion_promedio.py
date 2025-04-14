import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

# Calcular la calificación promedio
calificacion_promedio = tienda["Calificación"].mean()
calificacion_promedio2 = tienda2["Calificación"].mean()
calificacion_promedio3 = tienda3["Calificación"].mean()
calificacion_promedio4 = tienda4["Calificación"].mean()

# Crear un diccionario con las calificaciones formateadas a 2 decimales
dic_tiendas = {
    "Tienda 1": f"{calificacion_promedio:.2f}",
    "Tienda 2": f"{calificacion_promedio2:.2f}",
    "Tienda 3": f"{calificacion_promedio3:.2f}",
    "Tienda 4": f"{calificacion_promedio4:.2f}"
}

print(dic_tiendas)

# Crear una lista de tuplas con el número de tienda y la calificación promedio
data = [(tienda, calificacion) for tienda, calificacion in dic_tiendas.items()]

# Crear el DataFrame con las columnas "Tienda" y "Calificación Promedio"
df_tiendas = pd.DataFrame(data, columns=["Tienda", "Calificación promedio"])

# Guardar el DataFrame en un archivo CSV
df_tiendas.to_csv("./data/calificacion_promedio.csv", index=False)

if __name__ == "__main__":
    print("Calculando calificación promedio...")
   
