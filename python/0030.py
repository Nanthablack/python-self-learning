price = input()
m3, m11 = 0, 0
for i in price :
    m3 = (m3*10 + int(i))%3
    m11 = (m11*10 + int(i))%11
print(m3, m11)