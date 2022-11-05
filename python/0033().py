a = int(input())
n = list(map(int, input().split()))
dic_num = {}
for i in n :
    if i in dic_num.keys() : dic_num[i] += 1
    else : dic_num[i] = 1
maxVal = max(dic_num.values())
dict_sorted = sorted(dic_num.items())
for k, v in dict_sorted :
    if v == maxVal :
        print(k, end=' ')