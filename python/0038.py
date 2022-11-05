num = int(input())
anw = sorted(set({input() for i in range(num)}))
print(*anw, sep='\n')