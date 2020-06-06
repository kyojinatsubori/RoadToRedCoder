n,q=map(int,input().split())
act=[['N']]*q
follow=[['N']*n for _ in range(n)]
for i in range(q):
    act[i]=list(map(int,input().split()))
    if act[i][0]==1:
        follow[act[i][1]-1][act[i][2]-1]='Y'
    elif act[i][0]==2:
        for j in range(n):
            if follow[j][act[i][1]-1]=='Y':
                follow[act[i][1]-1][j]='Y'
    elif act[i][0]==3:
        tmp=[]
        for j in range(n):
            if follow[act[i][1]-1][j]=='Y':
                for k in range(n):
                    if follow[j][k]=='Y':
                        tmp.append(k)
        for j in tmp:
            follow[act[i][1]-1][j]='Y'
            follow[act[i][1]-1][act[i][1]-1]='N'
for i in range(n):
    print("".join(follow[i]))