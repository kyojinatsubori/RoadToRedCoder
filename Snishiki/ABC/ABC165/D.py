import math
A,B,N = map(int,input().split())

if N < B:
    print(math.floor(A*N/B))
else:
    print(math.floor(A*(B-1)/B))