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

texto = str(input('Ingrese el twitter: '))

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

#---------Estructuras de control --------------

respues = str(input('Es mujer?'))

if respues == 'si':
    genero = 'm'
else:
    genero = 'h'

# Uso del While
#Mostrar los números del 1 al 10 por pantalla
i = 1
while i<10:
    print(i)
    i = i + 1    # Se necesitas esta parte del codigo para que no se vaya al infinito


while True:
    print('Escribe 0 para salir')
    respuesta = int(input())
    if respuesta == 0:
        break

a = 1
while a < 15:
    print(a)
    a = a + 1

a = 1
while a <= 15:
    print(a)
    a = a + 1

#Programa

fin = 0
max = 1

while fin == 0:
    num = int(input('Ingrese un número. Para terminar, ingrese 0: '))

    if num == 0:
        fin = 1
    else:
        if num > max:
            max = num

print(f'El mayor valor ingresado fue: {max}')

num = 1
while num <=10:
    print(num)
    num += 1

i = 0
sum = 0

while i < 50:
    print(i)
    i = i+5
    sum = sum + i

print(f'Suma de los números múltiplos de 5 menores a 50 es: {sum}')

#El mismo programa incluyendo
num = int(input('Has que numero desee que el programa calcule los multiplos del 5'))
i = 0
sum = 0

while i < num:
    print(i)
    sum = sum + i
    i = i+5


print(f'Suma de los números múltiplos de 5 menores a 50 es: {sum}')

#Mostrar la tabla de multiplicar del número 7

num = 7
i = 0
while i < 13:
    print(f'{num} * {i} = {num*i}')
    i += 1

num = int(input('Ingrese la tabla a multiplicar'))
i = 0
while i < 13:
    print(f'{num} * {i} = {num*i}')
    i += 1


num_1 = int(input('Ingrese el primer numero: ')) # tome ha este numero como mi contador
num_2 = int(input('Ingrese el segundo número: '))
suma = 0

while num_1 <= num_2:
    if (num_1 % 2 == 0):
        print(num_1)
        suma = suma + num_1
    num_1 = num_1 + 1

print(f'La suma de numeros pares es: {suma}')

#Programa que cuenta cuantos numero pares hay

num_1 = int(input('Ingrese el primer numero: ')) # tome ha este numero como mi contador
num_2 = int(input('Ingrese el segundo número: '))
n_n_pares = 0

while num_1 <= num_2:
    if (num_1 % 2 == 0):
        print(num_1)
        n_n_pares = n_n_pares + 1
    num_1 = num_1 + 1

print(f'Hay {n_n_pares} pares')

#Programa que aprueba de usuario

edad = type(input('Ingrese su edad'))

if edad == str:
    while edad == int:
        edad = type(int('Esta ingresando letras, ingrese su edad'))


edad = type(input('Ingrese su edad'))
while edad == str:
    print('Error')
    edad = type(input('Ingrese su edad'))



while True:
    try:
        edad = int(input('Ingrese su edad'))
        print('número')
    except:
        ValueError