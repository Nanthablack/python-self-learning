a = int(input())
b = int(input())
c = int(input())
total = a + b + c
if total >= 0 and total <= 49:
    print("F")
elif total >= 50 and total <= 54:
    print("D")
elif total >= 55 and total <= 59:
    print("D+")
elif total >= 60 and total <= 64:
    print("C")
elif total >= 65 and total <= 69:
    print("C+")
elif total >= 70 and total <= 74:
    print("B")
elif total >= 75 and total <= 79:
    print("B+")
elif total >= 80 and total <= 100:
    print("A")