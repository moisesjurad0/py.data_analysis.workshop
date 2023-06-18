"""sumary_line."""

import pandas as pd

tabla = pd.read_csv(r'TablaEjemplo.csv')
type(tabla)  # <class 'pandas.core.frame.DataFrame'>

print(pd.__version__)
