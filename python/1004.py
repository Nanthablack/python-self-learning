Input = input().split()
Nc,Ns = int(Input[0]),int(Input[1])
data = dict()
for i in range(Ns) :
    add = input().split()
    data[add[1]] = add[0]
def method(data) :
    menu = [1,2]
    row = dict()
    res = []
    while menu[0] != 'X' :
        menu = input().split()
        if menu[0] == 'E' :
            if data[menu[1]] not in row :
                row[data[menu[1]]] = [menu[1]]
            else :
                row[data[menu[1]]].append(menu[1])
        temp = 'test'
        if menu[0] == 'D' :
            for i in row :
                if len(row[i]) != 0 :                    
                    res.append(row[i][0])
                    row[i].pop(0)
                    if len(row[i]) == 0 :
                        temp = i
                    break
            if temp != 'test' :
                row.pop(temp)
    res.append(0)
    return res
result = method(data)
for i in range(len(result)) :
    print(result[i])