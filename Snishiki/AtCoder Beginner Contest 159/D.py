N = int(input())
array = list(map(int, input().split()))
sameNum = [0]*(N)
sum = 0
# kを削除していないlistでの組み合わせを調べる
for i in range(N):
    sameNum[array[i]-1] += 1
for i in range(N):
    sum += sameNum[i]*(sameNum[i]-1)//2

for k in range(1, N+1):
    sumT = sum
    print(sumT - sameNum[array[k-1]-1] + 1)