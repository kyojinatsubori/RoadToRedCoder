# プリム法
import heapq
H,W = map(int,input().split())
sx,sy = map(int,input().split())
gx,gy = map(int,input().split())
ans = 0
nextL = [(1,0),(0,1),(-1,0),(0,-1)]
board = []
for i in range(H):
    board.append(list(map(int,input().split())))
q = []
used = [[0]*W for i in range(H)]
heapq.heappush(q, (0, sy-1, sx-1))
# 全部マイナスがけして管理するか
while len(q)>0:
    nowPP,nowY, nowX = heapq.heappop(q)
    # ここ忘れがち。まだused=0の時に入れた奴が生き残ってる可能性ある
    if used[nowY][nowX] == 0:
        used[nowY][nowX] = 1
        nowP = board[nowY][nowX]
        ans += nowP
        ans -= nowPP
        for a,b in nextL:
            nextY = nowY + a
            nextX = nowX + b
            if (0 <= nextY <= H-1) and (0 <= nextX <= W-1):
                if used[nextY][nextX] == 0:
                    nextP = board[nextY][nextX]
                    heapq.heappush(q, (-nowP*nextP, nextY, nextX))
print(ans)


