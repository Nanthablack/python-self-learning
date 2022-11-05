def binary(x):
    global lst
    global ans
    for n in range(1, x):
        bi = '{:b}'.format(n)[::-1]
        tempA = 1
        tempB = 0
        for k in range(len(bi)):
            if bi[k] == '1':
                tempA *= lst[k][0]
                tempB += lst[k][1]
        ans = min(ans, (abs(tempA-tempB)))
ans = 10**10
if __name__ == "__main__":
    n = int(input())
    global lst
    lst = []
    for x in range(n):
        lst.append(list(map(int,input().split())))
    binary(2**n)
    print(ans)