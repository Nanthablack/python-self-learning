lst = input().split()
last = []
for i in range(len(lst)):
    last.append(int(lst[i]))
last.sort(reverse = True)
check = list(set(last))
check.sort(reverse = False)
if len(check) == 1:
    print(check[0]*check[0])
elif len(check) == 2:
    print(check[0]*check[1])
else:
    x = min(check)
    check.remove(max(check))
    y = max(check)
    total = x * y
    print(total)