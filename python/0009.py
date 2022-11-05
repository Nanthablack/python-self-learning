number = [int(x) for x in input().split()]
word = list(input())
n = len(number)
number.sort()
a = number[ord(word[0]) - ord('A')]
b = number[ord(word[1]) - ord('A')]
c = number[ord(word[2]) - ord('A')]
print(a,b,c)