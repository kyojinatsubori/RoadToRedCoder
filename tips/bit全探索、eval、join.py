# ABC045
S = input()

sum = 0
for i in range(1 << len(S)-1):
    l = []
    for j in range(len(S)-1):
        if (i >> j) & 1 == 1:
            l.append(S[j])
            l.append("+")
        else:
            l.append(S[j])
    l.append(S[len(S)-1])
    sum += eval(''.join(l))
print(sum)
