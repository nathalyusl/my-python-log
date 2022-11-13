# <---- PROGRAMA_1 ---->
# Programa en Python que calcule el seno de x (sin x, donde x debe ir definido en radianes).
# Nombre: Diana Nathaly Altamirano Diaz
print('')
print('Programa_2')
print('')
print('En este acertijo los niños deben responder cuántos días tarda una rana en salir de un pozo de cierta profundidad, dado que de día avanza una determinada cantidad de metros y por la noche retrocede una cierta cantidad de metros.')
print('')

# a. Solicitar al usuario ingresar la profundidad en metros del pozo
flag = True
while flag:
    try:
        prof_pozo = int(input('Ingrese la altura en metros del pozo (en metros): '))
        if (type(prof_pozo) == int):
            flag = False
    except:
        print('Ingrese correctamente la profundidad del pozo.')
        flag = True

# b. Solicitar al usuario ingresar la cantidad de metros que la rana avanza de día
flag = True
while flag:
    try:
        ra_avanza = int(input('Ingrese la cantidad de metros que avanza de día (en metros):  '))
        if (type(ra_avanza) == int):
            flag = False
    except:
        print('Ingrese correctamente la profundidad del pozo.')
        flag = True

# c. Solicitar al usuario ingresar la cantidad de metros que la rana cae de noche
flag = True
while flag:
    try:
        ra_cae = int(input('Ingrese la cantidad de metros que cae de noche (en metros): '))
        if (type(ra_cae) == int):
            flag = False
    except:
        print('Ingrese correctamente la profundidad del pozo.')
        flag = True

#------------------------------------------------------------------------------------------------
# Algoritmo que calcula cuantos dias se demora en salir

sit_final = ra_avanza - ra_cae
dia = 0

while(sit_final <= prof_pozo):
    sit_final = (sit_final + ra_avanza) - ra_cae
    dia = dia+1
print(" ")
print(f"La rana se demora {dia} dias en salir")

