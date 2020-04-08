import math
X, Y = map(int,input().split())
max = X // 2

# bはxが２を増えるパターンの回数
for b in range(0, max+1):
    a = X - 2 * b
    if a * 2 + b == Y:
        break
    if b == max:
        print(0)
        exit()

ans = math.factorial(a + b) // math.factorial(a) // math.factorial(b)
ans = ans % (10**9+7)
print(ans)


