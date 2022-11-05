x,y = input().split()
lst = []
lst2 = []
resultlst = []
ans = []
last= ""
for i in range(int(x)):
    lst.append(input().split())
for i in range(int(x)):
    lst2.append(input().split())
for i in range(int(x)):
    for j in range(int(y)):
        resultlst.append(int(lst[i][j]) + int(lst2[i][j]))
    ans.append(resultlst)
    resultlst = []
for i in range(int(x)):
    for j in range(int(y)):
        last += str(ans[i][j]) + " "
    last.rstrip
    last += "\n"
print(last)