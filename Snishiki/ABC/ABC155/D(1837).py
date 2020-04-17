N,K = map(int,input().split())
A = list(map(int,input().split()))
times = []

for i in range(N-1):
    for j in range(i+1, N):
        times.append(A[i]*A[j])
times.sort()

print(times[K-1])
