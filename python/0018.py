x,y = input().split()
x = int(x)
y = int(y)
count = 0
lst = []
last =  []
for i in range(2,x+1):
    lst.append(i)
for i in range(2,x+1):
    for j in range(len(lst)):
        if lst[j] % i == 0:
            last.append(lst[j])
            lst[j] = 1
            count += 1
        if count == y:
            break
print(last[-1])