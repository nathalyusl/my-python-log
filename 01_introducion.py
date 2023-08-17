# Exercise_1
# Se puede usar comillas simples o compuesta

print('Hi how you doing')
print('Hi!')
print('Hola como estas')

# Exercise_2

print('Hola Diana')
#Error: Syntax error

#Exercise_3

print('Hola','Diana Nathaly') # union de cadenas del mismo tipo (string = cadena de caracteres)

print('Hola'+'Diana Nathaly')  #concatena sin dejar espacio entre hola y diana

print('Hola'+' '+'Diana Nathaly')

#_________Ejercicio_4_______________

# MEMORIA RAM: de uso volatil permite almacenar informacion mientras el computador este encendido
# mientras ejecutamos tenemos espacio para los programas.

# MEMORIA DE DISCO: uso permanente

# Operacion de asignacion
# i <- 2 el numero dos lo voy a guardar o almacenar en la variable i
# Mediante la asignacion almacenamos un valor en la memoria

i = 23        # integer (int)
i = 'Hola '   # string  (str)


# Operaciones aritmeticas

w = 100
i = 2 + w
i = i - 3

f = 5
i = 100 + f
print(i)

# Tipo de datos

x= 9
y= 7
z= x-y
ss= 'el resultado es: '

print(ss+str(z)) #convertir un entero a un string

# Exersises

msg='Mi edad en cinco años más será '
edad_hoy=21

print(msg + str(edad_hoy+5))

# Exercises

msg = 'El resultado es 2 * 3 + 4 - 12 ** 5 es:'
resul = 2*3+4-12**5

#TWO ways to present the results
print(msg + ' '+str(resul))
print(msg, resul)

a= 5
b= 3

c = a**b

print(f'El resultado de {a}**{b} es {c}') #Formato

#Exercises

a= '3.14159'   #string
b= 2.000       #float

c= float(a) + b
print(c)

#COMANDO input()

ss='El numero ingresado es: '
x= input()
print(ss + str(x))

print('Ingrese su edad:')
edad = input()
print('La edad ingresada es: ', int(edad))

edad1= int(input())   #Esta variable

#Programa que calcule el area de un rectangulo

print('Ingrese la base del rectangulo: ')
b = int(input())
print('Ingrese la altura del rectangulo: ')
a = int(input())
area = a*b
print(f'El area del rectangulo es: {area}')

#Other way correct the other program
b = float(input('Ingrese la base del rectangulo: '))
a = float(input('Ingrese la altura del rectangulo: '))
area = a*b
print(f'El area del rectangulo es: {area:.3f}') #FORMATO para que no salgan muchos decimales

# Operadores relacionales
a=23
b=4

er= a<b  # la variable er es una variable boolenana

type(er) # conocer que tipo de dato es la ariable

#Condicionales

if True:
    print('Estoy en el bloque de if')


if x<10:
    print("El número es menor a 10")
