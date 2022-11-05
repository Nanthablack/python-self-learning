import math as m
number = int(input())
diff = 2 - m.sqrt(3)
if number == 1:
    print("{:.6f}".format(2.0))
elif number%2 == 0:
    print("{:.6f}".format(number))
elif number == 3:
    print("{:.6f}".format(number - diff + 1))
elif number > 3:
    print("{:.6f}".format(number - 2 * diff + 1))