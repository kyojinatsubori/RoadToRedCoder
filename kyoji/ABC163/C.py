n=int(input())
p=list(map(int,input().split()))
a=[0]*n
for i in range(n-1):
    a[p[i]-1]+=1
for i in range(0,n):
    print(a[i])