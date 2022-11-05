def chain(a,b):
    res = True
    cnt = 0
    for i in range(len(a)):
    	if a[i] != b[i]:
    		cnt +=1
    		if cnt > 2 :
    			return False
    return res
def show(A):
    for i in range(len(A)-1):
        if chain(A[i],A[i+1]) == False:
            return A[i]
    return A[len(A)-1]
c = int(input())
n = int(input())
A = []
for i in range(n):
    A.append(input())
print(show(A))