years = [int(x) for x in input().split()]
for i in years:
    if i == -1:
        break
    workBee = 1
    soilBee = 0
    for j in range(i):
        TworkBee = 0
        TsoilBee = 0
        TworkBee += soilBee
        soilBee = 0
        TworkBee += workBee
        TsoilBee += workBee
        workBee = 0
        TworkBee += 1
        workBee += TworkBee
        soilBee += TsoilBee
    print(f"{workBee} {workBee + soilBee + 1}")