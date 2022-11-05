import math
jump = [int(i) for i in input().split()]
if jump[1] > jump[0]:
    print(int(math.ceil(jump[1]/jump[0])))
else:
    print(2)