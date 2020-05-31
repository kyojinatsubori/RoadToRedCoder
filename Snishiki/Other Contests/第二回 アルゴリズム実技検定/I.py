import copy
n=int(input())
a=map(int,input().split())
num=[0]*(2**n)
for i in range(n):
    for j in range(2**(n-i-1)):
        []