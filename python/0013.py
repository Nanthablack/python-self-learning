lst = []
for i in range(9):
    x = int(input())
    lst.append(x)
total = sum(lst)
for i in range(9):
    for j in range(i+1,9):
        if total - 100 == lst[i] + lst[j]:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(lst[k])