import pandas as pd

df = pd.read_csv('Data_frame/simple_data.csv')

print(df)

dt = pd.read_csv('Data_frame/african_crises.csv')

#Estadisticas
print(df.describe())
print('___')

#Los primeros diez datos
print(df.head(10))
print('___')

#Los ultimos 5 registros
print(df.tail(5))