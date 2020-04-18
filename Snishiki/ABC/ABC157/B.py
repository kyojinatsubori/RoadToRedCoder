A = [0]*9
A[0], A[1], A[2] = map(int, input().split())
A[3], A[4], A[5] = map(int, input().split())
A[6], A[7], A[8] = map(int, input().split())
N = int(input())
B = [0]*N
for i in range(N):
    B[i] = int(input())
if A[4] in B:
    if A[0] in B and A[8] in B:
        print("Yes")
        exit()
    if A[2] in B and A[6] in B:
        print("Yes")
        exit()
    if A[1] in B and A[7] in B:
        print("Yes")
        exit()
    if A[3] in B and A[5] in B:
        print("Yes")
        exit()
if A[0] in B and A[1] in B and A[2] in B:
    print("Yes")
    exit()
if A[6] in B and A[7] in B and A[8] in B:
    print("Yes")
    exit()
if A[0] in B and A[3] in B and A[6] in B:
    print("Yes")
    exit()
if A[2] in B and A[5] in B and A[8] in B:
    print("Yes")
    exit()

print("No")