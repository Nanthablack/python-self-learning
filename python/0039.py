import itertools
food = int(input())
f_food = int(input())
n_food = ([int(i) for i in input().split()])
num = []
for i in itertools.permutations(range(1,food+1)):
    if i[0] not in n_food:
        num.append(i)
for x in num:
    print(*x)