# <---- PROGRAMA_1 ---->
# Programa en Python que calcule el seno de x (sin x, donde x debe ir definido en radianes).
# Nombre: Diana Nathaly Altamirano Diaz
print('')
print('Programa_2')
print('')
print('Programa en Python que determine el monto final del ahorro ingresando con tres parámetros mencionados: Interes, ahorro mensual, meses')
print('')
# Captura y validación de datos ingresados

#INTERES
flag = True
while flag:
    try:
        inte = float(input('Ingrese el interes del banco: '))
        if (type(inte) == float):
            flag = False
    except:
        print('Ingrese correctamente el interes.')
        flag = True

#AHORRO MENSUAL

flag = True
while flag:
    try:
        ahorro = float(input('Ingrese el ahorro mensual: '))
        if (type(ahorro) == float):
            flag = False
    except:
        print('Error: Ingrese correctamente el monto.')
        flag = True

#MESES

flag = True
while flag:
    try:
        meses = int(input('Ingrese a cuantos meses desea realizar el ahorro: '))
        if (type(meses) == int):
            flag = False
    except:
        print('Error: Ingrese correctamente los meses.')
        flag = True

#Elaboracion del programa

#Imprimir en pantalla (Encabezados)
print('{:^2} {:^16}'.format('Mes', 'Total (al final del mes)'))

#Tranformo mi tasa para poder usarla
inte = inte * 0.01
ahorro_1 = ahorro + ((ahorro + 0) * inte)
print(ahorro_1)
ahorro_acum = 0.0
ahorro_aux= ahorro_1

for i in range(meses -1):
    ahorro_acum = ahorro + ahorro_aux + ((ahorro + ahorro_aux) * inte)
    ahorro_aux = ahorro_acum
    print(ahorro_acum)