N = int(input())
l = 0
r = 0
x = input().split()
total = 0
maximum = 0
last= ""
for i in range(len(x)):
    x[i] = int(x[i])
for i in range(N):
    total += x[i]
    if total < 0:
        total = 0
    else:
        if maximum < total:
            maximum = total
            r = i
total = 0
maximum = 0
for i in range(N-1,0,-1):
    total += x[i]
    if total < 0:
        total = 0
    else:
        if maximum <= total:
            maximum = total
            l = i
if maximum != 0:
    for i in range(l,r+1):
        last += str(x[i]) + " "
    print(last.rstrip())
    print(maximum)
else:
    print("Empty sequence")