from collections import deque
n,x,y = map(int,input().split())
maze = [["."]*403 for _ in range(403)]
for i in range(n):
    a,b = map(int,input().split())
    maze[b+201][a+201] = "#"
# yx
nl = [(1,0), (0,1), (-1,0),(0,-1),(1,1), (1,-1)]
dist = [[-1]*403 for _ in range(403)]
q = deque([])
q.append((201,201))
dist[201][201] = 0

while len(q)>0:
    cy, cx = q.popleft()
    if cy == y+201 and cx == x+201:
        break
    for ny, nx in nl:
            ny += cy
            nx += cx
            if (0 <= ny < 403) and (0 <= nx < 403):
                if dist[ny][nx] == -1 and maze[ny][nx] == ".":
                    q.append((ny,nx))
                    dist[ny][nx] = dist[cy][cx] +1
print(dist[y+201][x+201])



