# Visual Code Studio 
print('Used the first time visual studio code')
#Comando Type
a = 10
print(type(a))

a = 'hola'   #Asignacion dinamica solo en Phyton
print(type(a))

# Ejercicio

print('Ingresar un número: ')
b = int(input())

if type(b) == int:
    print('a es un entero')

c = input('Ingrese un número: ')

if type(c) == str:
    print('Es una cadena de texto')


# Uso de isdigit mirar si una cadena solo tiene digitos
# Me entrega un valor boolean 

num = input('Ingresa un numero: ')

if num.isdigit():
    print('Es un númeron entero')
else: 
    print('Ingreso otra cosa')


# Uso de isinstance(variable, tipo) 
# Me entrega un valor boolean 

numero = input('Ingresa un número :')

if isinstance(numero, int):
    print('Ingresaste una cadena de texto')
elif isinstance(numero, str):
    print('Ingresaste un número')
else:
    print('Ingresaste otra cosa')


# Uso de Assert 

ing = input('Ingrese un numero')

assert isintance(ing, int)  #'Error. El numero no es un entero'

