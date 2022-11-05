import math
x,y = input().split()
x = float(x)
y = float(y)
total = math.sqrt(x**2 + y**2)
print("%.6f"%total)