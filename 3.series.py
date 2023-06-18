"""sumary_line."""

import pandas as pd

tabla = pd.read_csv(r'TablaEjemplo.csv')
print(tabla)
type(tabla)  # <class 'pandas.core.frame.DataFrame'>

x1 = tabla['Nombre']
print(x1)
print(type(x1))  # <class 'pandas.core.series.Series'>

x2 = tabla['Edad']
print(x2)
print(type(x2))  # <class 'pandas.core.series.Series'>

x3 = tabla[['Nombre', 'País']]
print(x3)
print(type(x3))  # <class 'pandas.core.frame.DataFrame'>

print(pd.__version__)
