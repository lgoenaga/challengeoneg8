import pandas as pd
from main import tienda, tienda2, tienda3, tienda4

ventas_por_categoria = tienda.groupby('Categoría del Producto')['Precio'].sum()
ventas_por_categoria2 = tienda2.groupby('Categoría del Producto')['Precio'].sum()
ventas_por_categoria3 = tienda3.groupby('Categoría del Producto')['Precio'].sum()
ventas_por_categoria4 = tienda4.groupby('Categoría del Producto')['Precio'].sum()

# Convert the Series to a DataFrame for better formatting
ventas_df = ventas_por_categoria.reset_index()
ventas_df.columns = ['Categoría', 'Ventas Totales']  # Rename columns for clarity
ventas2_df = ventas_por_categoria2.reset_index()
ventas2_df.columns = ['Categoría', 'Ventas Totales']  # Rename columns for clarity
ventas3_df = ventas_por_categoria3.reset_index()
ventas3_df.columns = ['Categoría', 'Ventas Totales']  # Rename columns for clarity
ventas4_df = ventas_por_categoria4.reset_index()
ventas4_df.columns = ['Categoría', 'Ventas Totales']  # Rename columns for clarity

# Format 'Ventas Totales' as currency
ventas_df['Ventas Totales'] = ventas_df['Ventas Totales'].apply(lambda x: "${:,.2f}".format(x))
ventas2_df['Ventas Totales'] = ventas2_df['Ventas Totales'].apply(lambda x: "${:,.2f}".format(x))
ventas3_df['Ventas Totales'] = ventas3_df['Ventas Totales'].apply(lambda x: "${:,.2f}".format(x))
ventas4_df['Ventas Totales'] = ventas4_df['Ventas Totales'].apply(lambda x: "${:,.2f}".format(x))

# Display the formatted DataFrame
print("-" * 40)  # Print a line of 30 hyphens
print(ventas_df.to_string(index=False))  # Hide the index for cleaner output
print("-" * 40)  # Print a line of 30 hyphens
print(ventas2_df.to_string(index=False))  # Hide the index for cleaner output
print("-" * 40)  # Print a line of 30 hyphens
print(ventas3_df.to_string(index=False))  # Hide the index for cleaner output
print("-" * 40)  # Print a line of 30 hyphens
print(ventas4_df.to_string(index=False))  # Hide the index for cleaner output
print("-" * 40)  # Print a line of 30 hyphens

# Guardar los resultados en un archivo CSV
ventas_df.to_csv("./documents/ventas_por_categoria.csv", index=False)
ventas2_df.to_csv("./documents/ventas_por_categoria2.csv", index=False)
ventas3_df.to_csv("./documents/ventas_por_categoria3.csv", index=False)
ventas4_df.to_csv("./documents/ventas_por_categoria4.csv", index=False)

# Crear un archivo CSV y escribir los datos
with open("./data/ventas_categoria_totales.csv", "w") as f:
    # Escribir los datos de la Tienda 1
    f.write("Tienda 1\n")  # Título para la Tienda 1
    ventas_df.to_csv(f, index=False, header=True)  # Escribir el DataFrame de la Tienda 1

    # Escribir los datos de la Tienda 2
    f.write("\nTienda 2\n")  # Título para la Tienda 2
    ventas2_df.to_csv(f, index=False, header=True)  # Escribir el DataFrame de la Tienda 2

    # Escribir los datos de la Tienda 3
    f.write("\nTienda 3\n")  # Título para la Tienda 3
    ventas3_df.to_csv(f, index=False, header=True)  # Escribir el DataFrame de la Tienda 3

    # Escribir los datos de la Tienda 4
    f.write("\nTienda 4\n")  # Título para la Tienda 4
    ventas4_df.to_csv(f, index=False, header=True)  # Escribir el DataFrame de la Tienda 4

if __name__ == "__main__":
    print("Calculando ventas por categoría...")
   

