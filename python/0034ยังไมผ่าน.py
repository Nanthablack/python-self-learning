found = 0
A,B,C = input().split()
A = int(A)
B = int(B)
C = int(C)
for a in range(1,A+1):
    c = A/a
    if C < 0:
        CC = (-1) * C
    else:
        CC = C
    for b in range(-1*CC,CC+1):
        if b == 0:
            b += 1
        if C%B == 0:
            d = C/b
            if a*d+c*b == B:
                found = 1
                break
    if found == 1:
        break
if found == 1:
    print(a,b,c,d)
else:
    print("No Solution")