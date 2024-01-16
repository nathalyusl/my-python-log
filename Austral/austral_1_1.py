import math

math.pi

math.e

math.sqrt(4)

el_mundo_redondo = True
if el_mundo_redondo:
    print("La tiera es redonda")


x=1
z=3
x= (x+z)*2
y= x/3
m= x- y
z = y

text = 'Hello World'
r = text[6]
print(r)


text = 'Hello World'
print(text[6])

# You can also access string characters starting from the end of the string. The last character has an index of -1, the second to last -2 and so on.

text = 'Hello World'
print(text[-1])

# You can access the number of characters in a string with the built-in len() function.
text = 'Hello World'
print(len(text))

#Useful built-in function is type(), which returns the data type of a variable. Modify your print call to print the data type of text.

text = 'Hello World'
print(type(text))

shift = 3
print(type(shift))

# Caesar cipher. Specifically, you will take each letter in your message, find its position in the alphabet, take the letter located after
# 3 positions, and replace the original letter with the new letter.
#Start by finding the position of the first letter in the string. One way is to use the built-in find() function:
text = 'Hello World'
shift = 3
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(alphabet.find('a')) #imprime la posicion del caracter

index = alphabet.find(text[0])
print(index)

#find() returns the index of the matching character inside the string. If the character is not found, it returns -1. As you can see, the first
# character in text, uppercase "H", is not found, since alphabet contains only lowercase letters.
#You can transform a string into its lowercase equivalent with the lower() function. Add another print() call to print text.lower() and see the output.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
index = alphabet.find(text[0])
print(index)
print(text.lower())

#Then
index = alphabet.find(text[0].lower())
print(index)

#USE FOR

# for i in text:
# for is the keyword denoting the loop type. i is a variable that sequentially takes the value of the elements in text.
# The statement ends with a colon, :.

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = 0
for i in text:
    print(i)

nombre = "new york"
print(nombre[-2])