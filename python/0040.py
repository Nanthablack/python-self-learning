i = int(input())
anw = []
for x in range(i):
    num = int(input())
    if num == 2:
        anw.append("T")
    elif num % 2 == 0:
        anw.append("F")
    else:
        anw.append("T")
print(*anw,sep='\n') 