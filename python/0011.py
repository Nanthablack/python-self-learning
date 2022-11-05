lst = []
for i in range(10):
    lst.append(int(input())%42)
last = len(set(lst))
print(last)