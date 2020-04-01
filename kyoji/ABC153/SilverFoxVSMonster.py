n, d, a = map(int, input().split())
array = [0]*n
count = 0
for i in range(n):
    array[i] = list(map(int, input().split()))
array.sort()
while array:
    if array[0][1] <= 0:
        array.pop(0)
    else:
        for i in range(len(array)):
            if array[i][0] <= array[0][0] + 2 * d:
                array[i][1] -= a
        count += 1
print(count)