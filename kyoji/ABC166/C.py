n,m=map(int,input().split())
h=list(map(int,input().split()))
tenboudai=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    tenboudai[a-1].append(b-1)
    tenboudai[b-1].append(a-1)
count=0
for i in range(n):
    flag=0
    for j in tenboudai[i]:
        if h[i]<=h[j]:
            flag=1
    if flag==0:
        count+=1
print(count)