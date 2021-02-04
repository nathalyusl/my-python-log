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

eee = 'hello' + 'there'   # means 'concatenate'
print(eee)

