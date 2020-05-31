import queue
R,C = map(int,input().split())
sy, sx = map(int,input().split())
gy,gx = map(int,input().split())
maze = []
for i in range(R):
    maze.append(input())
# −１にすることで灰色かどうか判定する
dist = [[-1]*C for _ in range(R)]
dist[sy-1][sx-1] = 0
q = queue.Queue()
q.put([sy-1,sx-1])

while(not q.empty()):
    cy, cx = q.get()
    if cy == gy-1 and cx == gx-1:
        break
    # 上下左右のマスの確認,もうちょい綺麗にかけそう
    nl = [[cy-1, cx], [cy, cx-1], [cy+1, cx], [cy, cx+1]]
    for nyx in nl:
        # 今回は壁で囲まれている為>0,<R等のチェックは不要
        if maze[nyx[0]][nyx[1]] == "." and dist[nyx[0]][nyx[1]] == -1:
            q.put([nyx[0],nyx[1]])
            dist[nyx[0]][nyx[1]] = dist[cy][cx] + 1
print(dist[gy-1][gx-1])

