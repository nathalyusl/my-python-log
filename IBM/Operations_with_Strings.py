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

pattern = r"\d\d\d\d\d\d\d\d\d\d"
text = "My Phone number is 1234567890"
match = re.search(pattern,text)
if match:
    print("Match found")
else:
    print("No Match found")

print(match)










