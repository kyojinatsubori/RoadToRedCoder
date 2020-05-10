n,k = map(int,input().split())
A = list(map(int,input().split()))
count = 0
memo = [1]
his = [0]*n
his[0] += 1

for i in range(2*(10**5)+1):
    if his[A[i]] == 0:
        his[A[i]] += 1
        memo.append(A[i])
    else:
        A[i]

