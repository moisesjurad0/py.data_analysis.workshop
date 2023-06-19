import pandas as pd
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')
print(tabla.head())
print('---')

# by default index is a numeric colum before the first col
print(type(tabla.index))  # <class 'pandas.core.indexes.range.RangeIndex'>

# print the index 22
print(tabla.index[22])
# Index does not support mutable operations
# tabla.index[22] = 1

# set another column as index
print(tabla.set_index('Vendedor').head())
print('---')

# the changes to the index wasn't applied, are only as return values.
print(tabla.head())

print('---ver---')
print(pd.__version__)
