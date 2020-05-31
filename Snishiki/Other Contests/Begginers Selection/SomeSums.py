n, a, b = map(int,input().split())
answer = 0

for num in range(n+1):
    sum = 0
    for i in range(len(str(num))):
        sum += int(str(num)[i])
    if sum >= a and sum <= b:
        answer += num
print(answer)


