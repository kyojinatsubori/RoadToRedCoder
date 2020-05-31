n,k = map(int,input().split())
A = list(map(int,input().split()))
count = 0
memo = [1]
his = [0]*n
his[0] += 1
index = 0
i = 0
while his[A[i]-1] == 0 or count <k:
    his[A[i]-1] += 1
    memo.append(A[i])
    i = A[i]-1
    count += 1

index = memo.index(A[i])
roop=memo[index:]

if k>len(memo):
    k-=len(memo)
    k%=len(roop)
    print(roop[k])
else:
    print(memo[k])

