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
print('---')

# in order to make the changes permanent use in_place | this don't return
# a copy.
tabla.set_index('Vendedor', inplace=True)
print(tabla.head())

# reset the index
tabla.reset_index(inplace=True)
print(tabla.head())

# copy to a variable
mytable01 = tabla.set_index('Vendedor')
print(mytable01.head())

# the original table remains the same
print(tabla.head())

print('---ver---')
print(pd.__version__)
