lst = []
count = 0
for i in range(5):
    x = input().split()
    for j in range(4):
        count += int(x[j])
    lst.append(count)
    count = 0
maximum = max(lst)
index = 0
for i in range(len(lst)):
    if maximum == lst[i]:
        index = i+1
print(str(index) + " " + str(maximum))