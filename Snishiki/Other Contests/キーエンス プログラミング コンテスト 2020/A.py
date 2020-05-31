H = int(input())
W = int(input())
N = int(input())
answer = 0
if H >= W:
    answer = N // H
    if N % H != 0:
        answer += 1
else:
    answer = N // W
    if N % W != 0:
        answer += 1
print(answer)