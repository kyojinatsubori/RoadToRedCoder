from collections import deque
H,W = map(int,input().split())
maze = []
for i in range(H):
    maze.append(input())
nl = [(1,0), (0,1), (-1,0),(0,-1)]
ans = 0

def bfs(sy,sx):
    dist = [[-1]*W for _ in range(H)]
    q = deque([])
    q.append((sy,sx))
    dist[sy][sx] = 0
    maxd = 0
    while len(q)>0:
        cy, cx = q.popleft()
        for ny, nx in nl:
            ny += cy
            nx += cx
            if (0 <= ny < H) and (0 <= nx < W):
                if dist[ny][nx] == -1 and maze[ny][nx] == ".":
                    q.append((ny,nx))
                    dist[ny][nx] = dist[cy][cx] +1
                    if maxd < dist[ny][nx]:
                        maxd = dist[ny][nx]
    return maxd

for i in range(H):
    for j in range(W):
        if maze[i][j] == ".":
            maxn = bfs(i,j)
            if maxn > ans:
                ans = maxn
print(ans)