import pandas as pd
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')
print(tabla.head())
print('---')

# GROUP BY
# creates a group of DataFrames from a DataFrame
tabla.groupby('Región')  # <pandas.core.groupby.generic.DataFrameGroupBy

print(list(tabla.groupby('Región')))
