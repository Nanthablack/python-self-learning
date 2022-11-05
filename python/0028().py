score=[]
team=[[0,0,input()] for _ in range(4)]
for i in range (4):
    karnan=list(map(int,input().split()))
    team[i][1]=sum(karnan)
    score.append(karnan)
for i in range (3):
    for j in range (i+1,4):
        if score[i][j]==score[j][i]:
            team[i][0]+=1
            team[j][0]+=1
        elif score[i][j]>score[j][i]:
            team[i][0]+=3
        else:
            team[j][0]+=3
for k in sorted(team,reverse=True):
    print(f"{k[2]} {k[0]}")