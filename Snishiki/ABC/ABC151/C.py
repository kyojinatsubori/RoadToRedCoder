n,m = map(int,input().split())
l = [0]*n
cor = 0
pen = 0
for i in range(m):
    p,s = map(str,input().split())
    if s == "AC":
        if l[int(p)-1] != -1:
            cor += 1
            pen += l[int(p)-1]
            l[int(p)-1] = -1
    else:
        if l[int(p)-1] != -1:
            l[int(p)-1] += 1
print(cor,pen)