N = int(input())
A = list(map(int,input().split()))
ans = 0
for i in range(1, N):
    k = 1
    for j in range(A[i-1]+i+1, N+1):
        if A[j-1] == k:
            ans += 1
        k += 1

print(ans)

