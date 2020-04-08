N,M = map(int, input().split())
l = list(map(int, input().split()))

l.sort()
if l[-M] >= sum(l)/4/M:
    print("Yes")
else:
    print("No")