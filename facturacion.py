import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

total_tienda = tienda["Precio"].sum() + tienda["Costo de envío"].sum()
total_tienda2 = tienda2["Precio"].sum() + tienda2["Costo de envío"].sum()
total_tienda3 = tienda3["Precio"].sum() + tienda3["Costo de envío"].sum()
total_tienda4 = tienda4["Precio"].sum() + tienda4["Costo de envío"].sum()

dic_tiendas = {"Tienda 1": total_tienda, "Tienda 2": total_tienda2, "Tienda 3": total_tienda3, "Tienda 4": total_tienda4}
print(dic_tiendas)
df_tiendas = pd.DataFrame.from_dict(dic_tiendas, orient="index", columns=["Total"])
df_tiendas['Total'] = df_tiendas['Total'].apply(lambda x: "${:,.2f}".format(x))
df_tiendas.to_csv("./data/facturacion.csv", index=True)

if __name__ == "__main__":
    print("Calculando facturacion...")
   
