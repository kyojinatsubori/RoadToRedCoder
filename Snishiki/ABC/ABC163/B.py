N,M = map(int,input().split())
A = list(map(int, input().split()))

if N-sum(A) < 0:
    print("-1")
else:
    print(N-sum(A))
