small = 6
medium = 9
large = 20
lst = []
number = int(input())
if number < 6:
    print("no")
else:
    for i in range(number):
        for j in range(number):
            for k in range(number):
                if 6*i+9*j+20*k <= number:
                    lst.append(6*i+9*j+20*k)
    lst.sort(reverse = False)
    lst.pop(0)
    lst = list(set(lst))
    lst.sort(reverse = False)
    for i in range(len(lst)):
        print(lst[i])