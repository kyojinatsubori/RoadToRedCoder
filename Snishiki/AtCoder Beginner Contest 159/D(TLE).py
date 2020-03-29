N = int(input())
array = list(map(int, input().split()))
sameNum = [0]*(N)

for i in range(N):
    sameNum[array[i]-1] += 1

for k in range(1, N+1):
    answer = 0
    sameNumT = sameNum[:]
    sameNumT[array[k-1]-1] -= 1
    for l in range(N):
        answer += sameNumT[l]*(sameNumT[l]-1)//2
    print(answer)