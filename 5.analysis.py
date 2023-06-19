"""sumary_line."""

import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')

tabla.info()
print(tabla.head())


# COUNT
# ------

# counts ocurrences in a Column (Column "Vendedor") - Descendent
print(tabla.Vendedor.value_counts())

# counts ocurrences in a Column (Column "Vendedor") - Ascendent
print(tabla.Vendedor.value_counts(ascending=True))

# use "dropna" to drop nulls so that not count them
print(tabla.Vendedor.value_counts(dropna=True))

# SORT
# ------

# ordena una columna
print(tabla.Vendedor.sort_values())

# ordena toda la tabla, se usa by para determinar que columnas
# por defecto es ASCendet
print(tabla.sort_values(by=['Vendedor', 'Ganancia']))

# INDEXING
# ---------

# filtra columna por valor
print(tabla.Artículo == 'Gorras')
# filtra tabla por columna filtrada
print(tabla[tabla.Artículo == 'Gorras'])
# filtra tabla por 2 columna
print(tabla[(tabla.Artículo == 'Gorras') & (tabla.Región == 'Norte')])

# STRINGS
# ---------

# filtra columna por valor, pero manejandola como un str y contains
print(tabla.Vendedor.str.contains('Trevor'))

# filtra tabla por columna filtrada por contains
print(tabla[tabla.Vendedor.str.contains('Trevor')])

# filtra tabla por columna filtrada por startswith
print("TMP1----------")
print(tabla[tabla.Vendedor.str.startswith('T')])

print(pd.__version__)
