# Uso de Strings
name = "Michael Jackson"

# Como puedes ingresar a cada letra?

name[0] #Imprime 'M'
name[-1] # Imprimira la ultima letra 'n'

#________Slicing = Segmentacion_____________

name[1:3] #Imprimera 'ic' el intervalo de inicio es uno y el fin 3, recordar que el indice 3 no se incluiria.
name[1:] # Imprime 'ichael Jackson'
name[:8] # printea esto = 'Michael '
name[:-13] #Printea = 'Mi'

#________Stride = Salto_________________

name[::2]  # Inicio:Fin:Salto eso imprime 'McalJcsn'
name[1:9:3] # Resultado 'ia '

#________Uso LEN = Calcula cantidad de caracteres_______________

len(name)  # 15 caracteres

#____________Concatenar o combinar cadena________________

name = "Michael Jackson"
statement= name + " is the best"
print(statement)   #  resultado = Michael Jackson is the best

#___________ Operacion de multiplicacion_____________

operacion = 3*name  # resultado = 'Michael JacksonMichael JacksonMichael Jackson'
print(operacion)

#___________Strings:escapes sequences_______________

# Hacer una nueva linea \n

print("Michael Jackson \nis the best")  #Michael Jackson
                                        #is the best

# Tabulacion \t

print("Michael Jackson \tis the best")  #Michael Jackson 	is the best

# Poder escribir una barra \

print("Michael Jackson \\is the best") # Michael Jackson \is the best

# Variacion con r

print(r"Michael Jackson \is the best")


#______________USO DE UPPER OR LOWER ____________

a = "Thriller is the sixth studio album"
b = a.upper()
print(b)  #Resultado: THRILLER IS THE SIXTH STUDIO ALBUM

b= a.lower()
print(b)   # Resultado = thriller is the sixth studio album

#_______________USO DE REPLACE _____________

a= "Michael Jackson is the best"
b= a.replace("Michael","Janet")
c= a.replace("Jackson","Ambar")
print(b)
print(c)

album = "The BodyGuard is the best album"
ch_name = album.replace("BodyGuard","Equatorial")
print(ch_name)

#___________USO DEL FIND_________________

name = "Michael Jackson"
print(name.find("el"))   #Resultado= 5 la pocision del primer indice
print(name.find("1"))   #Resultado= -1 la cadena no fue encontrada

#__________________FORMATAER CADENA EN PYTHON__________________________

#------ % OPERADOR ___________#Forma mas antigua de formatear cadenas

name = "Jonathan"
age = 30
print("My name is %s and I am %d years old." %(name,age))

# %s ----> Este es un marcador de posición para una cadena.
# %d ----> Este es un marcador de posición para un entero.

# ______ F-strings _________#

x = 10 
y = 20
print(f"The sum of x and y is {x + y}")

#_____________Cadena Cruda "r" _______#

regular_string = "C:\new_folder\file.txt"
print(regular_string)

regular_string = r"C:\new_folder\file.txt"
print(regular_string)

#____________________________ USO DE SPLIT _________________________#

# Convierte una cadena en una lista de subcadenas.
# Si no hay un delimitador utiliza los espacios.
# maxsplit permite controlar cuantas divisones se realizan
  
     #_____ SPLIT: DIVIDIR POR ESPACIO (Delimitador por defecto)_________#

texto = "Hola mundo en Python"
resultado = texto.split()
print(resultado)    # ['Hola','mundo','en','Phyton']

nombre_com = "Julieta Margarita Perez Manila"
nom_dividido = nombre_com.split()
print(nom_dividido)      #['Julieta','Margarita','Perez',Manila']

     #_____ SPLIT: DIVIDIR POR UN DELIMITADOR ESPECIFICO _____________#

texto = "manzana,banana,cereza"
resultado = texto.split(",")
print(resultado)       # ["mazana","banana","cereza"]

    #_____ SPLIT:LIMITAR EL NUMERO DE DIVISIONES _______# 

texto = "uno dos tres cuatro cinco"
resultado = texto.split(" ",2)
print(resultado)   # ['uno','dos','tres cuatro cinco']

    #_____ SPLIT: DIVIDIR POR SALTO DE LÍNEA ________#

texto = "primera línea\nsegunda línea\ntercera línea"
resultado = texto.split("\n")
print(resultado)   # ['primera línea', 'segunda línea', 'tercera línea']

   #_____ SPLIT: DIVIDIR EN BASE A UN CONJUNTO DE DELIMITADORES _____#

import re      # se esta importando regular expression, permite trabajar con texto.
texto = "manzana;banana,pera"
resultado = re.split('[,;]',texto)
print(resultado) # ['manzana', 'banana', 'pera']

#_______________________ RegEX ___________________________#
   # Is a tool for matching and handling strings
   # Working with regular expressions "search", "split","findall", "sub"

   # ___________ Search _________________#

import re
texto = "The BodyGuard is the best album"

# Define the pattern to search for
pattern = r"Body"

# Use the search() function to search for the pattern in the string
result = re.search(pattern,texto)

#Check if a match was found
if result:
    print("Match found")
else:
    print("No Match found")

# Print
print(result)  # <re.Match object; span=(4, 8), match='Body'>
               # Es un objeto match

      #_____Several special sequences in RegEx _____#

#     Special Sequence               Meaning                                        Example

#           \d           Matches any digit character (0-9)                "123"         matches  "\d\d\d"

#           \D           Matches any non-digit character                  "hello"       matches "\D\D\D\D\D"

#           \w           Matches any word character                       "hello_word"  matches "\w\w\w\w\w\w\w\w\w\w"
#                        (a-z, A-Z, 0-9 and _ )

#           \W           Matches any non-word character                   "@#$%"        matches "\W\W\W\W"

#           \s           Matches any whitespace character                 "hello word"  matches "\w\w\w\w\w\s\w\w\w\w"
#                        (space, "\t" tab, "\n" newline, etc.)

#           \S           Matches any except whitespace or tab             "hello_word" matches "\S\S\S\S\S\S\S\S\S\S"

#           \b           Word boundary
#                        Coincide donde empieza o termina una palabra.    "cat"        matches "\bcat\b" = busca cat este sola o separada por espacios, puntuación o inicios/finales de línea
#                                                                                               \bcat  = busca cat que empiece una palabra
#                                                                                               cat\b  = busca cat que termine una palabra

#           \B           Not a word Boundary
#                        Coincide donde no hay límite de palabra. Está    "bobcat"     marches "\Bcat\B" = busca que cat este medio de una palabra.
#                        dentro de una palabra.                                                "cat\B" = coincide con cat cuando está seguida por letra/números.
#                                                                                              "\Bcat" = coincide cuando no está al inicio de una palabra, debe haber letras antes.

#__________ Ejercicio __________#

pattern = r"\d\d\d\d\d\d\d\d\d\d"     #este patron está buscando exactamente 10 dígitos
text = "My Phone number is 1234567890"
match = re.search(pattern,text)            #Busca en el texto una coincidencia con el patrón
if match:
    print("Match found")
else:
    print("No Match found")

print(match)                  #<re.Match object; span=(19, 29), match='1234567890'> indica la linea en donde se encontro también
print(match.group())         # Mostrará el número que encontró "1234567890"


pattern = r"\D\D\D\D\D"
text = "hello"
match = re.search(pattern,texto)
if match:
  print("Match found")
else:
  print("No Match found")

print(match)
print(match.group())  # Mostrará el número que encontró

#_______________ Ejemplo 1: Buscar todas las ocurrencias de un patrón ______________#

import re

texto = "Tengo 2 manzanas y 3 plátanos"
resultado = re.findall(r'\d+', texto)    #Busca todos los números de la cadena 
print(resultado)   # ['2','3']

# \d+ busca una o más cifras consecutivas y findall() devuelve todas las coincidencias en forma de lista. 

#___________________ Ejemplo 2: Remplazar texto con re.sub() _______________________#

import re 

texto = "Hola, mi número es 555-1234"
resultado = re.sub(r'\d{3}-\d{4}', 'XXX-XXXX', texto)  # Reemplaza el número de texto original por XXX-XXXX
print(resultado)   # Hola, mi número es XXX-XXXX

# \d{3}-\d{4} busca un patron específico de un número de teléfono, y sub() lo remplaza con el texto proporcionado.

import re

texto = "Mi contraseña es 98-7654" 
resultado = re.sub(r'\d{2}-\d{4}', '**-****', texto)
print(resultado)

#_________________ Ejemplo 3: Comprobar si una cadena sigue un patrón _______________#

import re 

texto = "abc123"
resultado = re.match(r'\w+\d+', texto) # Verifica si el texto empieza con letras y termina en números

if resultado:
  print("Coindecia encontrada", reultado.group())
else:
  print("No hay coincidencia")

# \w+ busca uno o más caracteres alfanuméricos y el _ , y \d+ busca uno o más dígitos.
# match() devuelve una coincidencia si el patrón esta al principio de la cadena. 
# match() Intenta coicidir el patrón desde el inicio si no lo encuentra al principio imprime "none"



# re.match()             Usarlo para validar formatos desde el inicio (fechas, códigos encabezados)
#                        Verificar si un texto comienza con una palabra clave
#                        Devuelve match o none

# re.search()            Usarlo cuando se quiera encotrar la primera coincidencia en cualquier parte del texto.
#                        Devuelve match o none   

# re.findall()           Obtener todas las coincidencias de un patron. 
#                        Devuelve Lista de strings 
#                        Contar o listar todas las apariciones de un pátron
#                        Extraer múltiples datos (correos, fechas, números, etc)


#___________________ Ejercicio combinado ________________________#

import re 

texto = "Cliente: Mario Casas, Email: mariocasas@gmail.com, Tel: 555-1234. Cliente: Ana Lopez, Email: ana_lopez@yahoo.com, Tel:555-5678"

#________ re.match ________# Saber si el texto empieza con "Cliente":

  resultado = re.match("Cliente", texto)
  
  # Forma ternararia de escribir el resultado
  print("match:", resultado.gruop() if resultado else "No match")
  
  # Forma larga de esribrilo
  
  if resultado:
    print("match:", resultado.group())
  else:
    print("match:","Not match")

#________ re.search ______#
# Busca en el texto y devuelve el email


  resultado =  re.search(r"\S+@\S+", texto)

  # Forma ternararia de escribir el resultado
  print("match:", resultado.group() if resultado else "No match")
  
  # Forma larga de esribrilo

  if resultado:
    print("match:", resultado.group())
  else:
    print("Not match")

#_______ re.findall ______# Encontrar todo los emails

resultado =  re.findall(r"\S+@\S+", texto)
print("uso de findall: ", resultado)

#____________________ Ejercicio: Divididr una cadena utilizando delimitadores _______________#

import re 

texto = "manzana,platáno;pera|cereza" 
resultado = re.split(r",;|",texto)  # usa varios delitadores
print(resultado)  

#____________________ Ejercicio: Extraer correo electrónico de un texto __________________#


import re

texto = "Mis correo electrónico son ejemplo@dominio.com y contacto@empresa.org"
resultado = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,0}') 
print(resultado)

# 1. r'...'       Texto crudo


# 2. [a-zA-Z0-9._%+-]+           Esto captura la parte real local del correo antes del arroba.
 
#.          [] : clase de caracteres.

#.          a-zA-Z : letras minúsculas y mayúsculas.

#.          0-9 : dígitos

#.          ._%+- : caracteres permitidos (punto, guion bajo, porcentaje, más, menos.

#.          + : uno o más de esos catácteres. 


# 3. @    Caracter literal con r'' lee todos los caracteres como son


# 4. [a-aZ-Z0-9.-]


# 5.  \.   Esconde el . literal, porque en regex el punto representa cualquier carecter, aqui queremos un punto real que se pare el dominio y el TLD


# 6. [a-zA-Z]{2,} Letras minúsculas o mayúsculas. 
#      {2,} : Busca una secuencia de letras mayúsculas o minúsculas que tenga mínimo 2 letras. 




#-------------------------------------------
# Equivalencias comunes en regex
#-------------------------------------------

#         Atajo           Equivale a                   Significa

#          \d               [0-9]                Cualquier dígito (número del 0-9)       

#          \D               [^0-9]               Cualquier caracter no numérico 

#          \w               [a-zA-Z0-9_]         Cualquier letra, número o guión bajo.

#          \W               [^a-zA-Z0-9_]        Cualquier carácter que no sea letra número o guión bajo

#          \s               espacio, tab,        Cualquier espacio en blanco
#                           salto de línea
#                           [ \t\n\r\f\v]

#          \S               lo conrario de \s    Cualquier caracter que no sea espacio


#---------------------------------------------
# Ejercicio de aplicación de las equivalencias
#---------------------------------------------
import re

texto = "Número: 123 y letras: abc"
print(re.findall(r'\d+', texto)) #123
print(re.findall(r'\D+',texto)) # ['Número: ', ' y letras: abc']


#----------------------------------------------------
# Ejercicio: Buscar palabras con longitud específica
#----------------------------------------------------

import re
texto = "Las palabras más cartas so la, de, y"
resultado = re.findall(r'\b\w{2}\b', texto)

#   \b: límite de palabra.

#   \w{2}: exactamente 2 caracteres alfanuméricos.

import re

texto = "Hoy es un día de mucho sol y paz total"
resultado = re.findall(r'\b\w{3}\b', texto)
print(resultado)
# Salida: ['Hoy', 'día', 'muy', 'sol', 'paz']

import re

texto = "Cada paso debe estar bien hecho y claro"
resultado = re.findall(r'\b\w{4}\b', texto)
print(resultado)
# Salida: ['Cada', 'paso', 'bien', 'hecho', 'claro']

import re
texto = "encontrar palabras de cinco letras"
resultado = re.findall(r'\b\w{5}\b',texto)
print(resultado)

import re
texto = "Buscar numero aqui 123"
resultado = re.findall(r'\d')

import re
texto = re.findall("      ")

def es_correo_valido(correo):
    patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(patron, correo))



