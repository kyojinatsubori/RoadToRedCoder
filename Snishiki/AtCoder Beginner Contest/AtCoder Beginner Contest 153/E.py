H, N = map(int,input().split())
AB = [0]*N
for i in range(N):
    AB[i] = list(map(int,input().split()))

for i in range(N):
    AB[i].append(AB[i][0]/AB[i][1])

AB.sort(key=lambda x: x[2])

rest = H % AB[-1][0]
damage = AB[-1][0]
magic = AB[-1][1]

for i in range(N):
    

    #AB[-1][0] - restが余剰分。
    #この分を差し引いた時により効率が上がるような物があれば
    #それと交換すれば良い。
    #