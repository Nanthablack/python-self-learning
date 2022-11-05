x,y = input().split()
x = int(x)
y = int(y)
lst = []
searchlst = []
indexlst = []
lstStack = []
lstStack2 = []
blank = []
blank2 = []
diaglst = []
diaglst2 = []
lstcheck = []
lstcheck2 = []
text = ""
row = x
col = y
last = ""
last2 = ""
checkdiag = ""
checkdiag2 = ""
answer = ""
for i in range(x):
  lstStack.append(blank)
for i in range(x):
  lst.append(input().lower())
search = int(input())
for j in range(search):
  searchlst.append(input().lower())
for i in range(len(lst)):
  for j in range(len(searchlst)):
    if searchlst[j] in lst[i] or searchlst[j][::-1] in lst[i]:
      a = lst[i].find(searchlst[j][0])
      indexlst.append(searchlst[j])
      indexlst.append(i)
      indexlst.append(a)
      indexlst.append(str("[]"))
add = 0
for i in range(y):
  for i in range(len(lst)):
    for j in range(len(lstStack)):
        lstStack[j].append(lst[i][add])
        break
  add += 1
s = x
lstStack = lstStack[0]
for j in range(len(lstStack)):
  if j == x:
    lstStack2.append(blank2)
    lstStack2.append(lstStack[j])
    x += s
  else:
    lstStack2.append(lstStack[j])
for i in range(len(lstStack2)):
  text += str(lstStack2[i])
lstStack2 = text.split("[]")
for i in range(len(searchlst)):
  for j in range(len(lstStack2)):
    if searchlst[i] in lstStack2[j] or searchlst[i][::-1] in lstStack2:
      b = lstStack2[j].find(searchlst[i][0])
      indexlst.append(searchlst[i])
      indexlst.append(b)
      indexlst.append(j)
      indexlst.append(str("[]"))
down = len(lst)-1
for i in range(len(lst)):
  last += ("|" * i) + lst[i] + ("|" * down) + " "
  down -= 1
down = len(lst)-1
for i in range(len(lst)):
  last2 += ("|" * down) + lst[i] + ("|") * i + " "
  down -= 1
last = last.split()
last2 = last2.split()
up = 0
for j in range((row+col)-1):
  for i in range(row):
    blank2.append(last[i][up])
  diaglst.append(blank2)
  blank2 = []
  up += 1
up = 0
for j in range((row+col)-1):
  for i in range(row):
    blank2.append(last2[i][up])
  diaglst2.append(blank2)
  blank2 = []
  up += 1
for i in range(len(diaglst)):
  for j in range(len(diaglst[i])):
    checkdiag += diaglst[i][j]
  lstcheck.append(checkdiag)
  checkdiag = ""
for i in range(len(diaglst2)):
  for j in range(len(diaglst2[i])):
    checkdiag2 += diaglst2[i][j]
  lstcheck2.append(checkdiag2)
  checkdiag2 = ""
for i in range(len(searchlst)):
  for j in range(len(lstcheck)):
    if searchlst[i] in lstcheck[j] or searchlst[i] in lstcheck[j][::-1]:
      indexlst.append(searchlst[i])
      
      indexlst.append(str("[]"))

  for j in range(len(lstcheck2)):
    if searchlst[i] in lstcheck2[j] or searchlst[i] in lstcheck2[j][::-1]:
      indexlst.append(searchlst[i])
      if j <= row-1:
        tail2 = row-1-j
        take2 = 0
        for k in range(len(lst[row-(j+1)])):
          if searchlst[i][0] == lst[tail2+take2][k]:
              lon2 = k
              break
          else:
            take2 += 1
        take2 = 0
        tail2 = tail2 + lon2
        indexlst.append(tail2)
        indexlst.append(lon2)
      else:
        for k in range(len(lstcheck2[j])):
          if searchlst[i][0] == lstcheck2[j][k]:
            tail22 = k
            lon22 = j - (row - 1) + tail22
            break
        indexlst.append(tail22)
        indexlst.append(lon22)
      indexlst.append(str("[]"))
for i in range(len(searchlst)):
  for j in range(len(indexlst)):
    if searchlst[i] == indexlst[j]:
      answer += str(indexlst[j+1]) + " " + str(indexlst[j+2]) + "\n"
print(answer)