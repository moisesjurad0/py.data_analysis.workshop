import pandas as pd
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')
print(tabla.head())
print('---')
print('---')
print('---')

# UNSTACK

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

# STACK
print(e.stack())
print('---')
print('---')
print('---')

print(e.stack('Región'))
print('---')
print('---')
print('---')

print(e.unstack())
print('---')
print('---')
print('---')

# fill_value, para rellenar NaN
print(e.unstack('Categoría', fill_value=0))
print('---')
print('---')
print('---')
