n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse = True)
if a[m-1] >= sum(a)*0.25/m:
    print("Yes")
else:
    print("No")