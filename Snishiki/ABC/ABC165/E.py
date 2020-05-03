N, M = map(int,input().split())

if N % 2 == 0:
    for i in range(1,M+1):
        print(i, N-(i-1))
else:
    for i in range(1,M+1):
        print(i, N-i)
