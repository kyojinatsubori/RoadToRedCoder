n,m=map(int,input().split())
route=[[float('inf')]*m for _ in range(m)]
route[0][0]=0
for i in range(m):
    a,b=map(int,input().split())
    route[a-1][b-1]=1
    route[b-1][a-1]=1
for i in range(n):
    