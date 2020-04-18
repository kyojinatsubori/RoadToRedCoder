k, n = map(int, input().split())
array = list(input().split())
array2 = []
for i in range(len(array)-1):
    array2.append(int(array[i+1]) - int(array[i]))
first = int(array[0]) + k - int(array[len(array)-1])
array2.append(first)
print(k - max(array2))
