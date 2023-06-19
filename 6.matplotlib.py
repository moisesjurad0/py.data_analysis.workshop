"""sumary_line."""
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')

print('---info---')
tabla.info()
print('---initial table head---')
print(tabla.head())
print('---')


# GRAPHS
# ------
print('---')
ali = tabla[tabla.Categoría == 'Comestibles']
print(ali.head())
print('---')

print(ali.Artículo.value_counts().head())
print('---')

ali.Artículo.value_counts().plot()  # por defecto es plot(kind='Line')
plt.show()
print('---')

# por defecto es plot(kind='Line')
ali.Artículo.value_counts().plot(kind='line', color='red')
plt.show()
print('---')

ali.Artículo.value_counts().plot(kind='bar')
plt.show()
print('---')

ali.Artículo.value_counts().plot(kind='barh')
plt.show()
print('---')

ali.Artículo.value_counts().plot(kind='pie')
plt.show()
print('---')


# Dispersion Ghraphics
tabla.head().plot(kind='scatter', x='Unidades', y='Ganancia')
plt.show()
print('---')

# Colores. Usa el parametro color
tabla.head().plot(kind='scatter', x='Unidades', y='Ganancia', color='green')
plt.show()
print('---')

# colormap. You can change colormap instead of color with some default
# values as e.g. jet & twilight
ali.Artículo.value_counts().plot(kind='pie', colormap='twilight')
plt.show()
print('---')

# sizes, use figsize to proportionally change sizes.
tabla.Artículo.value_counts().plot(kind='pie', colormap='twilight', figsize=(20, 10))
plt.show()
print('---')

print(pd.__version__)
