"""sumary_line."""

import pandas as pd

# skip 5 first rows from .csv file
tabla = pd.read_csv(r'ventasTotales.csv', skiprows=5)

# pd.set_option("display.max.columns", None)
print(tabla.to_string(max_rows=6))
print(type(tabla))  # <class 'pandas.core.frame.DataFrame'>


print(pd.__version__)
