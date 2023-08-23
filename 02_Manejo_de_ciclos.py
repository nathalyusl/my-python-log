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

bm ='No' in ('Sí','Si','sí','si') # esto me devuelve un valor booleano

# in = devuelve true si elemento se encuentra entro del otro elemento
# not in = devuelve true si el elemento no se encuentra dentro del otro elemento

if 1:
    print("Es uno")

if 0:                  #el cero es falso
    print('es cero')

#--------- PROGRAM ---------#
# Programa que identifica si un numero es par o impar

num = int(input('Ingrese un número'))

if (num%2 == 0):
    print(f'El número {num} es par')
else:
    print(f'El número {num} es impar')

#--------- PROGRAM ---------#
#Programa que utiliza la función len() para medir un texto

texto = input('Ingrese el twitter: ')

if len(texto) == 0:
    print('Escribe algo')
elif (len(texto) > 0 and len(texto)<28):
    print('ok')
else:
    print('texto muy larga')

saludo = 'Hola'
largo = len(saludo)
print(f'El largo de {saludo} es {largo}')

saludo= input('Ingrese un saludo')
largo = len(saludo)
print(f'El largo de {saludo} es {largo}')