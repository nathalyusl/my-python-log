area = 5
w = 8

if( area > 10):
    print('El area es mayor a 10')
    w = 11
else:
    if(area > 5):
        print('El area es mayor a 5')
        w=6
    else:
        print('El area es menor a 6')
        w = 1

print(str(w))