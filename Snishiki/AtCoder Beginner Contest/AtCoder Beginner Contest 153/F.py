from math import ceil
from collections import deque
count = 0
ans = 0

N, D, A = map(int, input().split())
Monster = [0]*N
for i in range(N):
    Monster[i] = list(map(int, input().split()))
Monster = [[x, ceil(h/A)] for x, h in Monster]
Monster.sort()
que = deque([])

for x,h in Monster:
    # 範囲外となったダメージを削除する
    while que and x > que[0][0]:
        a, b = que.popleft()
        count -= b
    # 範囲内で既に起きたダメージを受ける
    need = max(0, h-count)
    ans += need
    count += need
    # 爆発が届く限界と起きた回数を記録しておく
    que.append([x + 2*D, need])
print(ans)
