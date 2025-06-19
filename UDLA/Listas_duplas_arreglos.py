#____________LISTAS _________________#

clientes: ["Ana", "Pedro", "Lucia", "Manila"] #Pensar como una forma de organizar datos relacionados.
ventas: [200,300,450,250]

# Cada elemento en la lista tiene una posición, llamada índice, el índice comienza en cero.

# Imprimir el primer elemento de la lista clientes:

print(clientes[0]) #Resultado = Ana

# Imprimir el ultimo elemento de la lista aqui hay un truco el -1

print(clientes[-1]) #Resultado = Lucia

#Imprimir cada dos elementos

print(clientes[::2])

#Imprimir inicio, fin, salto

print(ventas[1:3:3])
print(ventas[0:3])