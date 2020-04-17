N,K = map(int,input().split())
count = 0

while N//K != 0:
    N = N//K
    count += 1
print(count+1)