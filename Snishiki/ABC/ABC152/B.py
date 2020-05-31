a,b = map(int,input().split())
ans = []
if a < b:
    for i in range(b):
        ans.append(a)
elif a >= b:
    for i in range(a):
        ans.append(b)
print(''.join(map(str, ans)))

