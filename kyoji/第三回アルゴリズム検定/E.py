n,m,q=map(int,input().split())
spr=[[0]*n for _ in range(n)]
for i in range(m):
    u,v=map(int,input().split())
    spr[v-1][u-1]=1
    spr[u-1][v-1]=1
c=list(map(int,input().split()))
for i in range(q):
    s=list(input().split())
    if s[0]=='1':
        print(c[int(s[1])-1])
        for i in range(n):
            if spr[int(s[1])-1][i]==1:
                c[i]=c[int(s[1])-1]
    else:
        print(c[int(s[1])-1])
        c[int(s[1])-1]=s[2]
