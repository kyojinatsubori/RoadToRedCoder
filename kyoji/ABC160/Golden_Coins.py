x = int(input())
count500 = 0
count50 = 0
while x >= 500:
    x -= 500
    count500 += 1
while x >=5:
    x -= 5
    count50 += 1
print(count500 * 1000 + count50 * 5)