import copy
N = int(input())
A = list(map(int,input().split()))
ans = []
for i in range(1,N+1):
    ia = copy.deepcopy(i)
    count = 1
    for j in range(N+1):
        if A[ia-1] == i:
            ans.append(count)
            break
        else:
            ia = A[ia-1]
            count += 1

print(' '.join(map(str,ans)))
