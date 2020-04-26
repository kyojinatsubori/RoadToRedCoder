from collections import deque
H, W = map(int, input().split())
maze = [0]*H
visited = [0]*H
for i in range(H):
    maze[i] = input()
    visited[i] = [-1]*W
arr0 = []
arr1 = []
arr2 = []

arr3 = []
arr4 = []
arr5 = []
arr6 = []
arr7 = []

arr8 = []
arr9 = []
arr10 = []
arr = []
ans = 0


for i in range(H):
    for j in range(W):
        if maze[i][j] == "S":
            arr0.append([i,j])
        elif maze[i][j] == "G":
            arr10.append([i,j])
        elif maze[i][j] == "1":
            arr1.append([i,j])
        elif maze[i][j] == "2":
            arr2.append([i,j])
        elif maze[i][j] == "3":
            arr3.append([i,j])
        elif maze[i][j] == "4":
            arr4.append([i,j])
        elif maze[i][j] == "5":
            arr5.append([i,j])
        elif maze[i][j] == "6":
            arr6.append([i,j])
        elif maze[i][j] == "7":
            arr7.append([i,j])
        elif maze[i][j] == "8":
            arr8.append([i,j])
        elif maze[i][j] == "9":
            arr9.append([i,j])
arr.append(arr0)
arr.append(arr1)
arr.append(arr2)
arr.append(arr3)
arr.append(arr4)
arr.append(arr5)
arr.append(arr6)
arr.append(arr7)
arr.append(arr8)
arr.append(arr9)
arr.append(arr10)


def bfs(maze, visited, sy, sx, gy, gx):
    queue = deque([[sy, sx]])
    visited[sy][sx] = 0
    while queue:
        y, x = queue.popleft()
        if [y, x] == [gy, gx]:
            return visited[y][x]
        for j, k in ([1, 0], [-1, 0], [0, 1], [0, -1]):
            new_y, new_x = y+j, x+k
            if visited[new_y][new_x] == -1 and 0 <= new_y < H and 0 <= new_x < W:
                visited[new_y][new_x] = visited[y][x] + 1
                queue.append([new_y, new_x])

    

if __name__ == "__main__":
    for i in range(10):
        count = []
        for j in arr[i]:
            sy , sx = j[0],j[1]
            for k in arr[i+1]:
                gy, gx = k[0], k[1]
                count.append(bfs(maze, visited, sy, sx, gy, gx))
        ans += min(count)

print(ans)