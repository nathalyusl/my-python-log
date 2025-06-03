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

x = int(input('Ingrese un número: '))
if x<10:
    print("El número es menor a 10")
else:
    print('El número es mayor a 10')

if False:
    print('estoy en el bloque del if')

area = 10
w= 8

# Program has a consumer date name, last name, age. Use just "if"

name = input('What is your name?')
last_name = input('what is your last name?')
age = int(input('How old are you?'))

if age<18:
    print(name, ', Remember to ask for your tutors autorization code ')

#Programa que comprueba si un numero es multipo de 3

num = int(input('Ingrese un número'))
if (num%3==0):
    print(f'El número: {num} es multiplo de 3')
else:
    print(f'El número: {num} no es multiplo de 3')

#Program to choose lunch menu

opcion = int(input('Choose your menu: 1. Hamburger 2. Pasta'))

if (opcion == 1):
    ham = int(input('Enter 1 If you want meet hamburger or 2 vegetarian hamburger'))
    if(ham==1):
        print('Preparing meet hamburger')
    else:
        print('Preparing vegetarian hamburger')
else:
    pas = int(input('Enter 1 if you want bologna pasta or 2 alfredo pasta'))
    if(pas==1):
        print('Preparing bologna pasta')
    else:
        print('Preparing alfredo pasta')

#Programa que seleciona rangos de edad solo con "If"

edad = int(input('Seleccione su rango de edad'
                 '1. Menor de 18 años'
                 '2. Entre 18 y 60 años'
                 '3. Mayor a 61 años'))

if(edad == 1):
    print('Para ingresar necesita estar acompañado de sus padres')

if(edad == 2):
    print('Presente su cédula e ingrese.')

if (edad == 3):
    print('Presente su cedula para un descuento del 20%')

# Otro forma de hacer el programa de rango de edad con if else

print('Seleccione su rango de edad')
print('1. Menor de 18 años')
print('2. Entre 18 y 60 años')
print('3. Mayor a 61 años')
edad = int(input())

if (edad==1):
    print('Para ingresar necesita estar acompañado de sus padres')
else:
    if(edad==2):
        print('Presente su cédula e ingrese.')
    else:
        print('Presente su cédula para un descuento del 20%')

# Programa

edad= int(input('Ingresa tu edad: '))

if(edad<18):
    print('No permitido')
else:
    if(edad<25):
        print('Reciba 1 bonus')
    else:
        if(edad<30):
            print('Reciba 2 bonus')
        else:
            print('Reciba 3 bonus')

#Programa utiliza if else y calcula el promedio de 2 notas y te dice si estas en el rango

nota_1 = float(input('Ingresa la nota 1: '))
nota_2 = float(input('Ingresa la nota 2: '))
promedio = ((nota_1 + nota_2)/2)

if (promedio >= 4.0): #recordar que cuando se utiliza float se debe colocar asi el numero
    print('Nota para aprobar el módulo')
else:
    if(promedio >= 3.0):
        print('Mejorar notas linea floja')
    else:
        print('Necesita tomar prueba de recuperacion o si no no hay posibilidades de aprobar')

#Programa

num_a = int(input('Ingrese un número entero: '))
num_b = int(input('Ingrese otro número entero: '))

if(num_a%num_b == 0):
    print(num_b, 'divide exactamente',num_a )
else:
    print(num_b, 'no divide a', num_a, 'en forma entera')

#Programa que resuelve el mismo problema con otro logica

num_a = int(input('Ingrese un número entero: '))
num_b = int(input('Ingrese otro número entero: '))

division = num_a/num_b
cociente = int(division)

if ((num_a - (cociente * num_b)) == 0):
    print(num_b, 'divide exactamente', num_a)
else:
    print(num_b, 'no divide a', num_a, 'en forma entera')

#Programa que solicita los valores de a,b y c de una ecuacion cuadratica de la forma:
print('Ingrese los valores a, b y c de una ecuación cuadrática')
a = int(input('Ingrese a'))
b = int(input('Ingrese b'))
c = int(input('Ingrese c'))

discriminante = b**2 -4*a*c

if(discriminante<0):
    print('No hay soluciones reales')
else:
    if(discriminante==0):
        x1= (-b + (discriminante**0.5))/(2*a)
        print(f'Hay una solución real y esta es: {x1}')
    else:
        x1 = (-b + (discriminante**0.5))/(2*a)
        x2 = (-b - (discriminante**0.5))/(2*a)
        print(f'Hay dos soluciones reales estas son: x1 = {x1} y x2 = {x2}')

#Programa que verifica si se puede viajar de la isla a A a la B por la condicion de puentes

print('Ingrese la condición de los puentes 0 no operativo y 1 operativo: ')
p1 = int(input('Puente 1:'))
p2 = int(input('Puente 2:'))
p3 = int(input('Puente 3:'))
p4 = int(input('Puente 4:'))
p5 = int(input('Puente 5:'))
p6 = int(input('Puente 6:'))
p7 = int(input('Puente 7:'))

if p1 == 1 and p4 == 1 and (p6 == 1 or p7 == 1):
    print('Si se puede viajar entre las islas')
elif p2 == 1  and (p6 == 1 or p7 == 1):
    print('Si se puede viajar entre las islas')
elif p3 == 1 and p5 == 1 and (p6 == 1 or p7 == 1):
    print('Si se puede viajar entre las islas')
else:
    print('No se puede viajar entre las islas')

#Programa: Identifica entre dos fechas, dia, mes, año cual ocurre antes o despues

print('Ingrese la primera fecha (dd/mm/año)')
dia_1 = int(input('Día: '))
mes_1 = int(input('Mes: '))
ano_1 = int(input('Año: '))

print('Ingrese la segunda fecha (dd/mm/año)')
dia_2 = int(input('Día: '))
mes_2 = int(input('Mes: '))
ano_2 = int(input('Año: '))

if (ano_1 < ano_2):
    print('La fecha 1 ocurrio antes que la fecha 2')
else:
    if(ano_2 < ano_1):
        print('La fecha 2 ocurrio antes que la fecha 1')
    else:
        if (mes_1 < mes_2):
            print('La fecha 1 ocurrio antes que la fecha 2')
        else:
            if(mes_2 < mes_1):
                print('La fecha 2 ocurrio antes que la fecha 1')
            else:
                if (dia_1 < dia_2):
                    print('La fecha 1 ocurrio antes que la fecha 2')
                else:
                    if (dia_2 < dia_1):
                        print('La fecha 2 ocurrio antes que la fecha 1')
                    else:
                        print('Fechas iguales')
# Asignación de variables 
edad = 30 # int
nombre = "Pedro" #str
altura = 1.75 #float

#Diccionarios = organizar datos complejos, almacena pares de clave-valor

persona = {"nommbre":"Pedro", "edad":30, "altura":1.75}

#Listas = colecciones ordenadas de elementos 

temperaturas=[30.8, 25.6, 12.3, 28, 6.5]

