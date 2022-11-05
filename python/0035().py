from itertools import combinations
def area(x1,y1,x2,y2,x3,y3):
    return abs(x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1)/2
n = int(input())
lisX,lisY=[],[]
ans=[]
for i in range(n):
    x,y=map(int,input().split())
    lisX.append(x)
    lisY.append(y)
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ans.append(area(lisX[i],lisY[i],lisX[j],lisY[j],lisX[k],lisY[k]))
print(f"{max(ans):.3f}")
