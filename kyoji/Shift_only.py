n = int(input())
listA = map(int, input().split())
listB = []
flag = 0
res = 0
for a in listA:
    b = 0
    while a % 2 == 0:
        a = a / 2
        b += 1
    listB.append(b)
print(min(listB))
