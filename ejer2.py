import pandas as pd

# Cargar los datos del archivo TSV
df = pd.read_csv('catastro.tsv', sep='\t')

# Filtrar los datos para el año 2014 y el barrio 'PALACIO'
df_palacio_2014 = df[(df['año'] == 2014) & (df['barrio'] == 'PALACIO')]

# Obtener el número de registros
num_registros = df_palacio_2014.shape[0]

# Imprimir el número de registros
print(f"Número de registros para el barrio 'PALACIO' en 2014: {num_registros}")