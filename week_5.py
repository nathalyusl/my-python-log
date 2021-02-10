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
'<='    # Grater than or equal to
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
