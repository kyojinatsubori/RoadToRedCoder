# 壁壊す＝コストと考えて、distのようにメモっていく。全部-1にしてスタートだけ0。
# ポイントは壁を壊さなくてもいいルートから優先探索(dfs)して、壁壊すのはqueueの後ろに入れていくやり方
# 別の解法としては、distを壊した回数ごとに記録してあげる方法[y][x][k]がある。k回壊してy,xにたどり着く最小手数をメモる（今回はTorFで十分）
from collections import deque
H,W = map(int,input().split())
sy, sx, gy, gx = 0,0,0,0
maze = []
for i in range(H):
    maze.append(input())
# スタートとゴールを見つける
for i in range(H):
    for j in range(W):
        if maze[i][j] == "s":
            sy,sx = i, j
        elif maze[i][j] == "g":
            gy,gx = i, j

# −１にすることで灰色かどうか判定する
dist = [[-1]*W for _ in range(H)]
dist[sy][sx] = 0
q = deque()
q.append((sy,sx))

while len(q)>0:
    cy, cx = q.popleft()
    # 上下左右のマスの確認,もうちょい綺麗にかけそう
    nl = [[cy-1, cx], [cy, cx-1], [cy+1, cx], [cy, cx+1]]
    for nyx in nl:
        if nyx[0] >= 0 and nyx[0] <= H-1 and nyx[1] >= 0 and nyx[1] <= W-1:
            if dist[nyx[0]][nyx[1]] == -1:
                if maze[nyx[0]][nyx[1]] == "#":
                    # []から()に変えたらMLE解消した
                    q.append((nyx[0],nyx[1]))
                    dist[nyx[0]][nyx[1]] = dist[cy][cx]+1
                else:
                    q.appendleft((nyx[0],nyx[1]))
                    dist[nyx[0]][nyx[1]] = dist[cy][cx]

if dist[gy][gx] <=2:
    print("YES")
else:
    print("NO") 

