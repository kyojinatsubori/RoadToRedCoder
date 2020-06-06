N = int(input())
A = []
for i in range(N):
    A.append(int(input()))

past = A[0]
for i in range(1, N):
    if past == A[i]:
        print("stay")
    elif past > A[i]:
        print("down "+ str(past-A[i]))
    else:
        print("up " + str(A[i]- past))
    past = A[i]
