import pandas as pd
'''
# Descargar los datos de los repositorios de github
url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

# Leer los datos de los repositorios de github
tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

# Guardar los datos en el archivo csv
tienda.to_csv("./data/tienda_1.csv", index=False)
tienda2.to_csv("./data/tienda_2.csv", index=False)
tienda3.to_csv("./data/tienda_3.csv", index=False)
tienda4.to_csv("./data/tienda_4.csv", index=False)
'''

tienda = pd.read_csv("./data/tienda_1.csv")
tienda2 = pd.read_csv("./data/tienda_2.csv")
tienda3 = pd.read_csv("./data/tienda_3.csv")
tienda4 = pd.read_csv("./data/tienda_4.csv")

'''
# Imprimir las columnas de los datos
    print("tienda columns:", tienda.columns)
    print("tienda2 columns:", tienda2.columns)
    print("tienda3 columns:", tienda3.columns)
    print("tienda4 columns:", tienda4.columns)
'''
print(tienda.head())

if __name__ == "__main__":
    print("Cargando datos...")
   
