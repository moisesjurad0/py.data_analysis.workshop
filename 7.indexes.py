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

# though this is a copy the original table it can reset its index and will
# have the initial numeric index with which wasn't born
print('---')
mytable01.reset_index(inplace=True)
print(mytable01.head())


# SORT
# the sorting is faster using sort_index cause it uses the index.
print('---')
mytable02 = tabla.set_index('Vendedor')
mytable02.sort_index(inplace=True)
print(mytable02.head())

mytable02.sort_index(inplace=True, ascending=False)
print(mytable02.head())
print('---')

# LOC
# indice basado en etiquetas. para que funcione tiene que setear el indice
# para que loc busque el valor ahí.
tabla.reset_index(inplace=True)  # reseteamos el original xsia
mytable03 = tabla.set_index('Vendedor')
print(mytable03.loc['Sarah Bond'].head())

# another way of do the same but without modifying index
print(tabla.loc[tabla.Vendedor == 'Sarah Bond'].head())

# ILOC
# Obtiene por indice numerico
print(mytable03.iloc[231])

# Obtiene varios por indice numerico
print(mytable03.iloc[[231, 49, 162, 101]])

# Obtiene rango por indice numerico
print(mytable03.iloc[7:14])

print('---ver---')
print(pd.__version__)
