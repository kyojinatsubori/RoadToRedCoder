N = int(input())
A = list(map(int, input().split()))
limit = N//2
maxi =[]
dp = [0]*N


if N % 2 == 0:
    print(max(sum(A[0::2]), sum(A[1::2])))
else:


