# 二分探索
# binsect.bisect_leftは同じ数字があったとき、左側の座標を返す（同じ数字の座標を返してるのと同義）
# binsect.bisect_rightは右側を返す。（ある数字以下〜を探す）
import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
A.sort()
C.sort()
ans = 0
for i in B:
    x = bisect.bisect_left(A, i)
    y = bisect.bisect_right(C, i)
    y = N - y
    ans += x*y
print(ans)