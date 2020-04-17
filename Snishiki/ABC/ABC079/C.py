ABCD = input()
res = 0
for i in range(1 << 3):
    l = []
    for j in range(3):
        if i >> j & 1 == 1:
            l.append(ABCD[j])
            l.append("+")
        else:
            l.append(ABCD[j])
            l.append("-")
    l.append(ABCD[-1])
    l = ''.join(l)
    res = eval(l)
    if res == 7:
        print(l + "=7")
        exit()



