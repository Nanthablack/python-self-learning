num = int(input())
anw = list([2**int(input()) for i in range(num)])
print(*anw, sep='\n')