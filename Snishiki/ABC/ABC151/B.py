n,k,m = map(int,input().split())
A = list(map(int,input().split()))
total = n*m
if total - sum(A) > k:
    print(-1)
else:
    if total - sum(A) <= 0:
        print(0)
    else:
        print(total - sum(A))