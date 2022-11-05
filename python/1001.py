def Add():
    n = input().split()
    A = []
    for i in range(int(n[0])):
        x = input()
        c = []
        for j in x:
            c.append(j)
        A.append(c)
    m = input().split()
    return A,m
def ans(A,x):
    for i in range(len(A)):
        if ((A[i][x] == 'O') or (A[i][x] == '#')) and (i != 0):
            A[i-1][x] = '#'
            return A
        elif ((A[i][x] == 'O') or (A[i][x] == '#')) and (i == 0):
            return A
    if (i == len(A)-1) and (A[len(A)-1][x] == '.'):
        A[len(A)-1][x] = '#'
        return A
def showans(A):
    for i in A:
        for j in i:
            print(j, end = '')
        print()
    
A,m = Add()
for j in range(len(m)):
    for i in range(int(m[j])):
        B = ans(A, j)
showans(B)