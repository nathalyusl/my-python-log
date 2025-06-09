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
statement= name + "is the best"
