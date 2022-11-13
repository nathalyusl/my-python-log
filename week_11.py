
# <---- PROGRAMA_1 ---->
# Programa en Python que calcule el seno de x (sin x, donde x debe ir definido en radianes).
# Nombre: Diana Nathaly Altamirano Diaz
print('')
print('Programa_1')
print('')
# Cargar librerias necesarias
import math
# Indica al usuario que hace el programa

print('El programa calacula el valor de sen(x) a través de la expasión de Tylor')
print('')

# Captura datos del usuario
# Valor de (x) debe comprobarse que sea un entero, ademas que debe ir definido en radianes.

flag= True
while flag:
    try:
        num = int(input('Ingrese el valor de x en grados entre 0 a 360 grados: '))
        if (type(num) == int):
            if (num >= 0 and num <= 360):
                flag= False
    except:
        print('El numero que ingresaste es incorrecto.')
        flag = True

#Transformo a radianes con la libreria
x = math.radians(num)

# Capturar el numero de terminos que deseo sumar es decir n
flag= True
while flag:
    try:
        n = int(input('Ingrese el numero de terminos que desea sumar'))
        if (type(n) == int):
            flag = False
    except:
        print('El numero que ingresaste es incorrecto.')

# Acumalador de los terminos
for i in range(n):