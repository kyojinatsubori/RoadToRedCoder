import math
from collections import deque
n=int(input())
a=[0]*n
sum=0
for i in range(n):
    a[i]=list(map(int,input().split()))
for i in range(n-1):
    for j in range(i+1,n):
        sum+=math.sqrt((a[i][0]-a[j][0])**2+(a[i][1]-a[j][1])**2)
print(sum*2/n)