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

df = pd.read_csv('Data_frame/athlete_events.csv')
