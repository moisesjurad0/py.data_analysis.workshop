import pandas as pd
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')
print(tabla.head())
print('---')
print('---')
print('---')

# GROUP BY
# creates a group of DataFrames from a DataFrame
tabla.groupby('Región')  # <pandas.core.groupby.generic.DataFrameGroupBy
print(list(tabla.groupby('Región')))
print('---')
print('---')
print('---')

# ITERATE BY GROUP BY
for group_key, group_value in tabla.groupby('Región'):
    print(group_key)
    print(group_value)
print('---')
print('---')
print('---')

print(type(group_key))  # str
print(type(group_value))  # pandas.core.frame.DataFrame
print('---')
print('---')
print('---')

# AGGR FUNCTIONS
print(tabla.groupby('Región').size())
print('---')
print('---')
print('---')

print(tabla.groupby(['Región', 'Vendedor', 'Ganancia']).agg(
    ['min', 'max', 'count']))
