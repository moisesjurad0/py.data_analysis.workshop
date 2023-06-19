"""sumary_line."""
import matplotlib.pyplot as plt
# %matplotlib inline
import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5, sep=';')

tabla.info()
print(tabla.head())


# GRAPHS
# ------
ali = tabla[tabla.Categoría == 'Comestibles']
ali.head()
ali.Artículo.value_counts()
ali.Artículo.value_counts().plot()  # por defecto es plot(kind='Line')


print(pd.__version__)
