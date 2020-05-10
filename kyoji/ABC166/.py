n,k=map(int,input().split())
d=[0]*k
a=[]
for i in range(k):
    d[i]=int(input())
    a.extend(list(map(int,input().split())))
a=set(a)
print(n-len(a))