a=2
b=3
c=4
d=12
e=5

resul= 2*3+4-12**5

print('El resultado de 2 * 3 +-12**5 es', resul)

print('Ingrese su edad')
mi_edad= int(input()) # primero se hace lo adentro captura de datos

print('Mi edad en 5 años es: ', mi_edad+5)

print('Programa que calcule el área de un rectángulo')
print('')
print('Ingrese la altura del rectángulo: ')
altura = int(input())
print('Ingrese la base del rectángulo: ')
base = int(input())
print('')
area = base * altura
print(f'El área es: {area}')


# Class Two

num = 1
sum = 0
contador = 0

while num != 0:
  num = int(input('Ingrese un número: '))
  sum = num + sum
  if num != 0:
    contador = contador + 1

  print(f'Ingresaste: {contador} Números que suma: {sum} ')


# Guia_de_ejericios_1

# Exercise_1
print('Esribe tu nombre, apellido y edad')
nombre = input()
apellido = input()
edad = int(input())

if edad < 18:
  print(f'Tu eres {nombre} {apellido} y tienes {edad} años.')

# Exercise_2: Multiplo del 3

print("Ingrese un numero para saber si es multiplo del 3 ")