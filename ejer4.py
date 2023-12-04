import pandas as pd

# Cargamos los datos del archivo TSV
df = pd.read_csv('catastro.tsv', sep='\t')

# Verificamos de los datos cargados
print("Datos cargados:")
print(df.head())

# Filtramos por año 2013 y uso Residencial
df_filtrado = df[(df['año'] == 2013) & (df['uso'] == 'Residencial')]

# Verificamos del filtrado
print("Número de registros después del filtrado:", len(df_filtrado))

# Seleccionamos los 15 primeros registros
df_filtrado = df_filtrado.head(15)

# Seleccionamos las columnas 'sup_cons' y 'valor_catastral' y creamos un nuevo DataFrame independiente
df_seleccionado = df_filtrado[['sup_cons', 'valor_catastral']].copy()

# Añadimos la columna 'valor_medio_m2'
# Aquí añadimos una comprobación para evitar la división por cero
df_seleccionado['valor_medio_m2'] = df_seleccionado['valor_catastral'] / df_seleccionado['sup_cons'].replace(0, 1)

# Mostramos el resultado
print("Resultado:")
print(df_seleccionado)