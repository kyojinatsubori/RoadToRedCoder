n, a, b = map(int, input().split())
i = 1
ans = 0
sum_list = []
while i <= n:
    s = str(i)
    array = list(map(int, s))
    if sum(array) >= a and sum(array) <= b:
        ans += i
    i += 1
print(ans)