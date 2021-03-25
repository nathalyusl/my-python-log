# Chapter Two: Variables and Expressions
# 2.1 Expression
# Reserved words: don't uses this words for name functions, don't name classes, don't name variables.
words = ['false', 'class', 'return', 'is', 'finally',
         'none', 'if', 'for', 'lambda', 'continue',
         'true', 'def', 'from', 'while', 'nonlocal',
         'and', 'del', 'global', 'not', 'with',
         'as', 'elif', 'try', 'or', 'yield',
         'assert', 'else', 'import', 'pass'
         'break', 'except', 'in', 'raise']

# Variables: Python, find us a spare piece of memory somewhere and given it a label of x, and put 12.2 in it.
x = 12.2
y = 14

print(x)

# Python variable name rules (Algunas reglas de nomenclatura): ovid use underscores because Python tends to use
# underscores for its own internal purposes
# Case sensitive

good_variables_list = ['spam', 'eggs', 'spam23', '_speed']

bad_variables_list = ['23spam', '#sing', 'var.12']

different_variables_list = ['spam', 'Spam', 'SPAM']   # eye! these all are different variable names

# Sentences or Lines: x: variable, "=" or "+": operator, '2': constant, print(): function.

x = 2       # Assignment statement
x = x + 2   # Assignment with expressions
print(x)    # Print statement

# Name the variables using a technique called "Mnemonic"

a = 35.0     # this is good but isn't mnemonic
b = 12.50
c = a * b
print(c)

# Mnecomic means that we choose a variable name that makes sense (sentido) for what we're using it for.

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)

# Assignment Statements: are not like mathematics, Equal '=' means equality

x = 0.6
x = 3.9 * x * (1 - x)

# Expressions part 2
# numeric Expressions
'+'      # addition
'-'      # subtraction
'*'      # multiplication
'/'      # division
'**'     # power
'%'      # remainder: me entrega el resto de una division.

xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)

# Order of evaluation
gg = 4
nn = 1 + (2 * 3) - (gg / (5 ** 6))

# Operator Precedence rules: Parenthesis, power, multiplication division, addition, left to right

tt = 1 + 2 ** 3 / 4 * 5
print(tt)

# Type

ddd = 1 + 4               # means 'addition'
print(ddd)

eee = 'hello ' + 'there' # means 'concatenate'
eee = eee + ' ' + str(1)
print(eee)

type(eee)

type('hello')
<class 'str'>

type(1)
<class 'int'>

temp = 98.6
type(temp)
<class 'float'>

# Type conversions

print(float(99) + 100)

i = 42
type(i)

f = float(i)
print(i)

print(int(99.8) + 45)

print( 4 / 2)
print(9 / 2)
print(99 / 100)
print(10.0 / 2.0)
print(99.0 / 100.0)

# String conversations
b = '123'
r = int(b) + 1

# User "input"

nam = input('who are you?')
print('welcome', nam)

# Get the name of the file and open it
name = input('Enter file:')
handle = open(name, 'r')

# Count word frequency
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts(word) = counts.get(word, 0) + 1

# Find the most common word
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

# All done
print(bigword, bigcount)

# write first code (in, work, out)
# Converting User Input (The european elevator converter app)
# Convert elevator floors
inp = input('Europe floor?')    #impre el mensaje luego se detiene y espera.
usf = int(inp) + 1
print('US floor' , usf)

# The code below almost works

name = input("Enter your name")
print("Howdy")


# Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Use 35 hours and a
# rate of 2.75 per hour to test the program (the pay should be 96.25). You should use input to read a string and float()
# to convert the string to a number. Do not worry about error checking or bad user data.
# This first line is provided for you

hrs_float = float(("Enter Hours:")
rate_float = float(input("Rate per hour:"))
print('Pay: ' + str(hrs_float * rate_float))

time_hour

