# 順列生成する関数あるんだった・・・・・
N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))
numP = 1
numQ = 1
for i in range(N-1):
    cou = 1
    time = P[i]-1
    for j in range(1,N-i):
        cou = cou*j
    for j in range(0,i):
        if P[j]< P[i]:
            time -= 1
    numP += time*cou
for i in range(N-1):
    cou = 1
    time = Q[i]-1
    for j in range(1,N-i):
        cou = cou*j
    for j in range(0,i):
        if Q[j]< Q[i]:
            time -= 1
    numQ += time*cou
print(abs(numP-numQ))