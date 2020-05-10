n = int(input())
x=[0]*n
l=[0]*n
t=[0]*n
for i in range(n):
    x[i],l[i]=map(int,input().split())
    t[i]=[x[i],l[i]]
t=sorted(t,key=lambda x:x[0]+x[1])
right=t[0][0]+t[0][1]
count=1
for i in range(1,n):
    if t[i][0]-t[i][1]>=right:
        count+=1
        right=t[i][0]+t[i][1]
print(count)