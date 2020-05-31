N,K = map(int,input().split())
R,S,P = map(int,input().split())
T = input()
memo = [""]*N
ans = 0
for i in range(N):
    if i >= K:
        if T[i] == "r":
            if memo[i-K] == "p":
                if i+K <= N-1:
                    memo[i] = T[i+K]
            else:
                memo[i] = "p"
                ans += P
        elif T[i] == "s":
            if memo[i-K] == "r":
                if i+K <= N-1:
                    memo[i] = T[i+K]
            else:
                memo[i] = "r"
                ans += R
        else:
            if memo[i-K] == "s":
                if i+K <= N-1:
                    memo[i] = T[i+K]
            else:
                memo[i] = "s"
                ans += S
    else:
        if T[i] == "r":
            memo[i] = "p"
            ans += P
        elif T[i] == "s":
            memo[i] = "r"
            ans += R
        else:
            memo[i] = "s"
            ans += S
print(ans)

