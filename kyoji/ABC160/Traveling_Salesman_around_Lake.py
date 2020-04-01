k, n = map(int, input().split())
array = [int(i) for i in input().split()]
ans = []
for i in range(n - 1):
    ans.append(array[i+1] - array[i])
ans.append(array[0] + k - array[n-1])
print(sum(ans) - max(ans))