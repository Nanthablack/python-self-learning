row = int(input())
col = row - 1 if row % 2 == 0 else row
midCol = int(col / 2) + int(col % 2)
midRow = int(row / 2) + int(row % 2)
line = [""] * row
for i in range(midRow):
    li = list("-" * col)
    li[(midRow - 1) - i] = li[(midRow - 1) + i] = '*'
    line[i] = ''.join(li)
    line[(row - 1) - i] = ''.join(li)
print('\n'.join(line))