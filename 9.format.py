import pandas as pd
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')
print(tabla.head())
print('---')
print('---')
print('---')

# STACK

cat = tabla[
    (tabla.Vendedor == 'Sarah Bond') &
    (
        tabla.Categoría.str.contains('Vestimenta|Comestibles')
    ) |
    (
        (tabla.Categoría == 'Vestimenta') |
        (tabla.Categoría == 'Comestibles')
    )
]
print(cat)
print('---')
print('---')
print('---')

c = cat.groupby(['Artículo', 'Categoría', 'Región']).size()
print(c)
print('---')
print('---')
print('---')

d = c.unstack('Categoría')
print(d)
print('---')
print('---')
print('---')

e = c.unstack('Región')
print(e)
print('---')
print('---')
print('---')
