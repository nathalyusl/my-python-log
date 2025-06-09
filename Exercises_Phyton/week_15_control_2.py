# <-------------- CONTROL_2 ------------>
# Resuelva el problema expuesto en un único script en Python.
# Nombres: Diana Nathaly Altamirano Diaz / Nicolas Rebolledo
print('')
print('___________PROGRAMA_____________')
print('')
print('Este programa permite ingresar dos deportes y determina si la diferencia '
      'entre las alturas de los jugadores es significativamente distinta.')
print('')

import pandas as pd

df = pd.read_csv('../Data_frame/athlete_events.csv')

# Solicitud de 2 deportes al usuario y validacion
sport = data_interesante['Sport'].unique()
print(sport)

sport.sort()

#Validación del primer deporte
A = 'Ninguna'
while A not in sport:
  print('\nDeportes disponibles: {}\n'.format( ', '.join(sport) ))
  A = input("Ingrese un deporte: ").title()
  if A not in sport:
    print('El deporte que deseas consultar no se encuentra en la base de datos. Por favor elegir los que estan en la lista.\n')

#Validación del segundo deporte
B = 'Ninguna'
while B not in sport:
  print('\nDeportes disponibles: {}\n'.format( ', '.join(sport) ))
  B = input("Ingrese otro deporte: ").title()
  if B not in sport:
    print('El deporte que deseas consultar no se encuentra en la base de datos. Por favor elegir los que estan en la lista.\n')



# Validacion cuando no tienen coicidencia de años
if years == []:
  print('')
  print('Resultado:')
  print(f'El deporte 1.{A} y el 2.{B} no se llevaron acabo en un mismo año.')
