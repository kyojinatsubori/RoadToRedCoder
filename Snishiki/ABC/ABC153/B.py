H ,N = map(int, input().split())
A = [0]*N
A = list(map(int, input().split()))

if H > sum(A):
    print("No")
else:
    print("Yes")