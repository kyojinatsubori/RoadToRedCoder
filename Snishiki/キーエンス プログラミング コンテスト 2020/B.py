N = int(input())
Xl = [0]*N
Ll = [0]*N
area = []
for i in range(0, N):
    Xl[i], Ll[i] = map(int, input().split())
for i in range(0, N):
    area.append(list(range(Xl[i]-Ll[i]+1, Xl[i]+Ll[i])))
print(area)
print(area[0][1])