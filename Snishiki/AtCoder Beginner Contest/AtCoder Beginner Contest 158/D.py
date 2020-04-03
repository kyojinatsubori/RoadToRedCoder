S = input()
Q = int(input())
que = [0]*Q
count = 0
flag = True
flist = []
llist = []

for i in range(Q):
    que[i] = list(map(str, input().split()))
for i in que:
    if len(i) == 1:
        count += 1
        flag = not flag
    else:
        if i[1] == '1' and flag:
            flist.append(i[2])
        elif i[1] == '2' and not flag:
            flist.append(i[2])
        elif i[1] == '1' and not flag:
            llist.append(i[2])
        else:
            llist.append(i[2])

F = ''.join(flist)
L = ''.join(llist)

if count % 2 == 1:
    S = S[::-1]
    L = L[::-1]
    print(L + S + F)
else:
    F = F[::-1]
    print(F + S + L)
