def change(T,i):
    if i == 'F':
        temp1 = T["top"]
        temp2 = T["front"]
        temp3 = T["back"]
        temp4 = T["bottom"]
        T["top"] = temp3
        T["front"] = temp1
        T["back"] = temp4
        T["bottom"] = temp2
    elif i == 'B':
        temp1 = T["top"]
        temp2 = T["front"]
        temp3 = T["back"]
        temp4 = T["bottom"]
        T["top"] = temp2
        T["front"] = temp4
        T["back"] = temp1
        T["bottom"] = temp3
    elif i == 'L':
        temp1 = T["top"]
        temp2 = T["left"]
        temp3 = T["right"]
        temp4 = T["bottom"]
        T["top"] = temp3
        T["left"] = temp1
        T["right"] = temp4
        T["bottom"] = temp2
    elif i == 'R':
        temp1 = T["top"]
        temp2 = T["left"]
        temp3 = T["right"]
        temp4 = T["bottom"]
        T["top"] = temp2
        T["left"] = temp4
        T["right"] = temp1
        T["bottom"] = temp3
    elif i == 'C':
        temp1 = T["front"]
        temp2 = T["left"]
        temp3 = T["back"]
        temp4 = T["right"]
        T["front"] = temp4
        T["left"] = temp1
        T["back"] = temp2
        T["right"] = temp3
    elif i == 'D':
        temp1 = T["front"]
        temp2 = T["left"]
        temp3 = T["back"]
        temp4 = T["right"]
        T["front"] = temp2
        T["left"] = temp3
        T["back"] = temp4
        T["right"] = temp1
    return T
A = []
n = int(input())
for i in range(n):
    A.append(input())
ans = []
for i in A:
    T = {"top": 1, "front": 2, "left": 3, "right": 4, "back": 5, "bottom": 6}
    for j in i:
        T = change(T,j)
    ans.append(T["front"])
for i in ans:
    print(i, end = ' ')