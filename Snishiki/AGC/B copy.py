from collections import deque
N = int(input())
p = list(map(int, input().split()))
thea = [[1]*N for i in range(N)]
NN = N**2
ans = 0
nb = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def bfs(sx, sy):
    destroy = [[-1] * N for _ in range(N)]
    q = deque([(sx, sy)])
    destroy[sx][sy] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in nb:
            nx = x + dx
            ny = y + dy
            if 0 <= nx and nx < N and 0 <= ny and ny < N:
                if destroy[nx][ny] == -1:
                    if thea[nx][ny] == 1:
                        destroy[nx][ny] = destroy[x][y] + 1
                        q.append((nx, ny))
                    else:
                        destroy[nx][ny] = destroy[x][y]
                        q.appendleft((nx, ny))
            else:
                return destroy[x][y]

for i in p:
    i -= 1
    sho = i//N
    ama = i%N
    if sho == 0 or sho == N-1 or ama == 0 or ama == N-1:
        thea[sho][ama] = 0
    else:
        ans += bfs(sho, ama)
        thea[sho][ama] = 0

print(ans)
