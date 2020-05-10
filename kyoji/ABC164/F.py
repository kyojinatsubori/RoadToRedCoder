n=int(input())
s=map(int,input().split())
t=map(int,input().split())
u=map(bin,input().split())
v=map(bin,input().split())
ans=[0]*n
for i in len(s):
    row=[0]*n
    if s[i]==0:
        row[i].append(u[i].replace(1,2))
    else:
        row[i].append(u[i].replace(0,2))
    ans[i]=row
for i in len():