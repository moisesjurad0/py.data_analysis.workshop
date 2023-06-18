"""sumary_line."""

import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5)
print(tabla)
type(tabla)  # <class 'pandas.core.frame.DataFrame'>

print(pd.__version__)
