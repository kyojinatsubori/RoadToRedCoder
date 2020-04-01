n = int(input())
array = list(map(int, input().split()))
Alice_list = []
Bob_list = []
array.sort(reverse=True)
i = 0
while i < len(array):
    if(i % 2 == 0):
        Alice_list.append(array[i])
    else:
        Bob_list.append(array[i])
    i += 1
print(sum(Alice_list) - sum(Bob_list))