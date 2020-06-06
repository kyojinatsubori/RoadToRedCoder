H,W = map(int,input().split())
c = []
ans = 0
for i in range(10):
    c.append(list(map(int,input().split())))
maze = []
for i in range(H):
    maze.append(list(map(int,input().split())))

for k in range(10):
    for i in range(10):
        for j in range(10):
            c[i][j] = min(c[i][j], c[i][k]+c[k][j])

for i in maze:
    for j in i:
        if j != -1:
            ans += c[j][1]
print(ans)
