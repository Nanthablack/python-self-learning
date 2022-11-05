x,y = input().split()
x = int(x)
y = int(y)
while True:
    if x > y:
        x -= y
    elif y > x:
        y -= x
    else:
        break
print(x)