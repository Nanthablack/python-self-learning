dim = input().split()
counter = 0
for i, e in enumerate(dim):
    dim[i] = int(dim[i])
while dim != [1, 1, 1]:
    j = dim.index(max(dim))
    if dim[j] % 2 == 1: dim[j] -= 1
    dim[j] = dim[j]/2
    counter += 1
print(counter)