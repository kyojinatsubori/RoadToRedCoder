H, W = map(int, input().split())

if H !=1 and W !=1:
    answer = H * W // 2
    if H * W % 2 != 0:
        answer += 1
    print(answer)
else:
    print(1)
