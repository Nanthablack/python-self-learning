text = list(input())
text.append(" ")
check = ['a','e','i','o','u']
for i in range(len(text)-1):
    if text[i] in check and text[i+1] == 'p' and text[i+2] in check:
        text[i+1] = 1
        text[i+2] = 1
last = ""
for i in range(len(text)):
    if text[i] == 1:
        continue
    else:
        last += text[i]
print(last)