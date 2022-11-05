number = int(input())
lst = input().split()
last = []
zero = []
total = ""
for i in range(len(lst)):
    if int(lst[i]) == 0:
        zero.append(int(lst[i]))
    else:
        last.append(int(lst[i]))
last.sort(reverse = False)
total += str(last[0])
if len(zero) != 0:
    for i in range(len(zero)):
        total += str(zero[i])
    for i in range(1,len(last)):
        total += str(last[i])
else:
    for i in range(1,len(last)):
        total += str(last[i])
print(total)
