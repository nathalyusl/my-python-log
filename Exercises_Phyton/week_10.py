#Uso de librerias

import math

# help(math)

math.pow(2,3)

# Factorial 

math.factorial(5)

#Uso 
import math

num = int(input('Ingrese un número: '))
expo = int(input('Ingrese el número de iteraciones: '))

acum = 0 
for i in range(0,expo+1):
  acum = acum + (math.pow(num,i)/ math.factorial(i))

print(acum)

# La lista son muy flexibles y puede ser una desventaja 
lista = [1,2,3]
print(lista)

lista[2] = 'Miguel'
print(lista)

#Agregar un dato a la lista 
lista.append('Hola')
print(lista)

import numpy as np

a = np.random.random([10, 4])

print(a)