# 謎に苦戦した・・・
# √Nまで見れば全探索できるやん・・・　
# 小さいほう入れる時はifとか書かずにmin使おう
import math
N = int(input())
ans = float('inf')
for i in range(1,math.ceil(math.sqrt(N)+1)):
    if N % i == 0:
        j = N//i
        if ans > i+j-2:
            ans = i+j-2
print(ans)

