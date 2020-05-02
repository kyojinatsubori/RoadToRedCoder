import math
X = int(input())
ans = 0
newX = 100
while newX < X:
    newX = math.floor(newX * 1.01)
    ans += 1
print(ans)