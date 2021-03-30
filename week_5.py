# Chapter Three: conditional Code
# Coditional Statements: choose the options
# COnditional steps
x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finis')

# Comparison Operators

'<'     # Less than
'<='    # less than or equal to
'=='    # Equal to
'>='    # Grater than or equal to
'>'     # Greater than
'!='    # not equal

# EYE '=' es una declaración de asignación

x = 5
if x ==5:
    print('Equals 5')

if x > 4:
    print('Grater than 4')

if x >= 5:
    print('Greater than or equal 5')

if x < 6:
    print('Less than 6')

if x <= 5:
    print('less than or equal 5')

if x != 6:
    print('Not equal 6')

# One-way Decisions

x = 5
print('Before 5')
if x == 5:
    print('Is 5')
    print('Is Still 5')
    print('Third 5')
print('afterwards 5')
print('Before 6')
if x == 6:
    print('Is 6')
    print('Is still 6')
    print('Third 6')
print('Afterwards 6')

# increase / maintain after if or for
# decrese to indicate end of block

x = 5
if x > 2:
    print('Bigger than 2')
    print('still bigger')
print('Done with 2') # only sequential code

for i in range(5):
    print(i)
    if i > 2:
        print('Bigger than 2')
    print('Done with i', i)
print('All Done') # only sequential code

# Nested Decisions

x = 42
if x > 1:
    print('More than one')
    if x < 100:
        print('Less than 100')
print('All Done')

# Two- way Decision

x = 4
if x > 2:
    print('Bigger')
else:
    print('Smaller')
print('All Done')

# More conditional Statements: Patrones de ejecución condicional un poco más complejos que podemos construir.
# elif is a combination to "else" and "if"
# Multi-way: the rule is one of the three  will run, and the other two will not.

if x < 2:
    print('small')
elif x < 10:
    print('Medium')
else:
    print('LARGE')
print('All done')

if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
elif x < 100:
    print('Huge')
else:
    print('Ginormous')

# Try and except

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1   # es un código que python ejecutará si algo sale mal

print('first', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)


astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# Sample try/except

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

# Practice

if x == 0:
    print("Good")

age = int(input('¿How all are you?')
if age > 18:
    print('Es usted mayor de edad')
else age < 18:
    print('Es usted menor de edad')
print('Good bay')

age = int(input('¿How all are you?'))
if age < 130:
    pass                  #esta orden le dice a Python que no tiene que hacer nada
else:
    print('Wou! I dont believe it!')
print(f'Usted dice que tiene {age} años.')

millas = int(input('Ingrese las millas'))
if millas == 80:
    pass
else:
    print('Millas correctas')
print(f'Usted tiene {age} millas')

print(f'Usted posee {millas} millas')

print(f'Usted tiene {age} millas')

print(f'Usted tiene {millas} millas')

print(f'Usted tiene {millas} millas')
