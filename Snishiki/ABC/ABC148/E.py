N = int(input())
i = 5
ans = 0
if N %2 == 0:
    for j in range(10**8):
        num = N//(i*2)
        if num == 0:
            break
        else:
            ans += num
            i = i*5

print(ans)


