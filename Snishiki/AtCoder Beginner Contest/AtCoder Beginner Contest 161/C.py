N,K = map(int, input().split())
ans = 0

ans = N % K
if ans > abs(ans - K):
    ans = abs(ans - K)
print(ans) 
