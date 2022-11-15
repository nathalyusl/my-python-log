ss = "El número ingresado es: "
x = input()
y = float(x) + 2

print(ss + str(y))    # "+" concatena cadena o las suma solo se concatena str

# <-------- Exercises ----------->
print("Ingrese un número decimal: ")
x = input()
y = float(x) + 2.2
aa = "El número decimal sumado 2.2 es: "

print(aa + str(y))   #si "y" no se cambia a str lo que pasara es que al concatenar dará un error.

