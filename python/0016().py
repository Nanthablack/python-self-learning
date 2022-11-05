num = int(input().strip())
sol = input().strip()
def a_ans(count):
    temp = count % 3
    if temp == 0:
        return "A"
    elif temp == 1:
        return "B"
    elif temp == 2:
        return "C"
def b_ans(count):
    temp = count % 4
    if temp == 0 or temp == 2:
        return "B"
    elif temp == 1:
        return "A"
    else:
        return "C"
def c_ans(count):
    temp = count % 6
    if temp == 0 or temp == 1:
        return "C"
    elif temp == 2 or temp == 3:
        return "A"
    else:
        return "B"
score = [0] * 3
for i in range (num):
    correct = sol[i]
    if correct == a_ans(i):
        score[0]+=1 
    if correct == b_ans(i):
        score[1]+=1 
    if correct == c_ans(i):
        score[2]+=1 
max_score = max(score)
print(max_score)
if(score[0] == max_score):
    print("Adrian")
if(score[1] == max_score):
    print("Bruno")
if(score[2] == max_score):
    print("Goran")