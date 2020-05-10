import collections
n=int(input())
a=list(map(int,input().split()))
b=[i+a[i]+1 for i in range(n)]
c=[i-a[i]+1 for i in range(n)]
count=0

    count+=c.count(b[i])
print(count)