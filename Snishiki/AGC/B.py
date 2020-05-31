from collections import deque
N = int(input())
p = list(map(int, input().split()))
thea = [[1]*N for i in range(N)]
NN = N**2
ans = 0

def maze(sy, sx):
    dist = [[-1]*N for _ in range(N)]
    dist[sy][sx] = 0
    q = deque()
    q.append((sy,sx))
    while len(q)>0:
        cy, cx = q.popleft()
        # 上下左右のマスの確認,もうちょい綺麗にかけそう
        nl = [(cy-1, cx), (cy, cx-1), (cy+1, cx), (cy, cx+1)]
        for nyx in nl:
            ny, nx = nyx
            if ny >= 0 and ny <= N-1 and nx >= 0 and nx <= N-1:
                if dist[ny][nx] == -1:
                    if thea[ny][nx] == 1:
                        q.append((ny,nx))
                        dist[ny][nx] = dist[cy][cx]+1
                    else:
                        q.appendleft((ny,nx))
                        dist[ny][nx] = dist[cy][cx]
            else:
                return dist[cy][cx]

for i in p:
    i -= 1
    sho = i//N
    ama = i%N
    if sho == 0 or sho == N-1 or ama == 0 or ama == N-1:
        thea[sho][ama] = 0
    else:
        ans += maze(sho, ama)
        thea[sho][ama] = 0

print(ans)
