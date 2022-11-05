check = input()
ball = [1,0,0]
ans = 0
for i in range(len(check)):
    if check[i] == "A":
        ball[0],ball[1] = ball[1],ball[0]
    if check[i] == "B":
        ball[1],ball[2] = ball[2],ball[1]
    if check[i] == "C":
        ball[0],ball[2] = ball[2],ball[0]
for i in range(3):
    if ball[i] == 1:
        ans = i + 1
        break
print(ans)