N, X, Y = map(int, input().split())
ks = [0]*(N-1)
for A in range(1,N):
    for B in range(A+1,N+1):
        if B - A > abs(X -A) + abs(Y - B) + 1:
            ks[B-A-1] -= 1
            ks[abs(X -A) + abs(Y - B)] += 1
for k in range(1,N):
    print(N - k + ks[k-1])