"""sumary_line."""

import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')

tabla.info()
print(tabla.head())

# counts ocurrences in a Column (Column "Vendedor") - Descendent
print(tabla.Vendedor.value_counts())

# counts ocurrences in a Column (Column "Vendedor") - Ascendent
print(tabla.Vendedor.value_counts(ascending=True))

# use "dropna" to drop nulls so that not count them
print(tabla.Vendedor.value_counts(dropna=True))

print(pd.__version__)
