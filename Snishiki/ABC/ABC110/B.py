n,m,x,y = map(int,input().split())
xx = list(map(int,input().split()))
yy = list(map(int,input().split()))
if x < y:
    for i in range(x+1, y+1):
        if max(xx) < i and min(yy) >= i:
            print("No War")
            exit()

print("War")