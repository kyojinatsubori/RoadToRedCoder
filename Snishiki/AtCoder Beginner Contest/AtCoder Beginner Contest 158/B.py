N, A ,B = map(int, input().split())
C = N // (A+B)
answer = C * A
answer += min(A, N%(A+B))
print(answer)