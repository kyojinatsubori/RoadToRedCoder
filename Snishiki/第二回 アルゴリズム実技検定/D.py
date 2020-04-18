S = input()
one = []
two = []
three = []
for i in range(len(S)):
    if S[i] not in one:
        one.append(S[i])
for i in range(len(S)-1):
    if S[i]+S[i+1] not in two:
        two.append(S[i]+S[i+1])
for i in range(len(S)-2):
    if S[i]+S[i+1]+S[i+2] not in three:
        three.append(S[i]+S[i+1]+S[i+2])

for i in two:
    nx = i[0] + "."
    xn = "." + i[1]
    if nx not in two:
        two.append(nx)
    if xn not in two:
        two.append(xn)

for i in three:
    nnx = i[0] + i[1]+ "."
    nxn = i[0] + "." + i[2]
    xnn = "." + i[1] + i[2]
    if nnx not in three:
        three.append(nnx)
    if nxn not in three:
        three.append(nxn)
    if xnn not in three:
        three.append(xnn)
print(len(one)+1 + len(two)+len(three))

