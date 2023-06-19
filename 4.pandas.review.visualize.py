"""sumary_line."""

import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')

# pd.set_option("display.max.columns", None)
print(tabla.to_string(max_rows=6))

print(type(tabla))  # <class 'pandas.core.frame.DataFrame'>

# cantidad de filas y columnas
# -----------------------------
# debes configurar el separador del DataFrame "sep" si tienes un separador
# que no es coma, sino no cogerá las columnas.
print(tabla.shape)

# por defecto muestra las primeras 5 filas
print(tabla.head())

# tb puede recibir un parametro de cantidad de filas.
print(tabla.head(3))

# por defecto muestra las ULTIMAS 5 filas
print(tabla.tail())

# por defecto muestra las ULTIMAS 5 filas
print(tabla.tail(3))

print(pd.__version__)
