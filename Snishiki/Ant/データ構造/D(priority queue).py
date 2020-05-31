import heapq
N = int(input())
a = list(map(int,input().split()))
fa = a[:N:]
ba = list(map(lambda x: x*(-1), a[2*N::]))
heapq.heapify(fa)
heapq.heapify(ba)
sumf = sum(fa)
sumb = sum(ba)
suml = [sumf]

k = -2

for i in range(N, 2*N):
    heapq.heappush(fa, a[i])
    sumf += a[i]
    sumf -= heapq.heappop(fa)
    suml.append(sumf)

suml[-1] += sumb

for j in range(2*N-1, N-1, -1):
        heapq.heappush(ba, -a[j])
        sumb -= a[j]
        sumb -= heapq.heappop(ba)
        suml[k] += sumb
        k -= 1
    


print(max(suml))


    
