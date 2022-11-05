x,y,z = input().split()
x = int(x)
y = int(y)
z = int(z)
if z - y == 1 and y - x == 1:
    print(0)
else:
    if z - y > 1 and y - x == 1:
        print(z-y-1)
    elif y - x > 1 and z - y == 1:
        print(y-x-1)
    else:
        if z - y > y - x:
            print(z-y-1)
        else:
            print(y-x-1)