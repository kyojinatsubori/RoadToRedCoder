H, W = map(int, input().split())
maze = [0]*H
visited = [0]*H
for i in range(H):
    maze[i] = input()
    visited[i] = [0]*W

for i in range(H):
    for j in range(W):
        if maze[i][j] == "s":
            sh, sw = i, j
        elif maze[i][j] == "g":
            gh , gw = i, j

stack = [(sh, sw)]
visited[sh][sw] = 1

while stack:
    nh , nw = stack.pop()
    for nexth, nextw in [(nh+1, nw), (nh-1, nw), (nh, nw-1), (nh , nw +1)]:
        if 0 <= nexth < H and 0 <= nextw < W and visited[nexth][nextw] == 0 and maze[nexth][nextw] != "#":
            visited[nexth][nextw] = 1
            stack.append((nexth, nextw))

if visited[gh][gw] == 1:
    print("Yes")
else:
    print("No")
