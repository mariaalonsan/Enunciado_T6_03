import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargamos el archivo .tsv, especificando que el separador es un tabulador
df = pd.read_csv('catastro.tsv', sep='\t')

# Vamos a estableces la columna "año" como índice
df.set_index('año', inplace=True)

# Mostramos las 5 primeras primeros filas
print(df.head())


