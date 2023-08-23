#Programa

resp = input('Le gustan los dulces?')

if (resp == 'Sí' or resp == 'Si' or resp == 'si' or resp == 'sí'):
    print('A mi tambien')


#__________ Other way ________#

resp = input('Le gustan los dulces?')

if (resp == 'Sí'):
    print('A mi tambien')
elif (resp == 'Si'):
    print('A mi tambien')
elif (resp == 'si'):
    print('A mi tambien')
elif (resp == 'sí'):
    print('A mi tambien')

#--------- Other way -----------#
#

if input('Te gustan los dulces?: ') in ('Sí','Si','sí','si'):
    print('A mi también')

pregunta = input('Te gustan los dulces?: ')
if pregunta in ('Sí','Si','sí','si'):
    print('A mí tambien')

#--------- PROGRAM ---------#
# Programa que identifica si un numero es par o impar

num = int(input('Ingrese un número'))

if (num%2 == 0):
    print('El número es par')
else:
    print('El número es impar')