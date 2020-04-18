R,G,B,N = map(int,input().split())
count= 0
sum = 0

for i in range(N//R +1):
    sum = 0
    sum += i * R
    for j in range((N-sum) // G +1):
        Ssum = sum
        Ssum += j * G
        if (N - Ssum) % B == 0:
            count += 1

print(count)

    