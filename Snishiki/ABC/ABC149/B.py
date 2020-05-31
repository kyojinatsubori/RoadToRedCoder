a,b,k = map(int,input().split())
if k >= a+b:
    print(0,0)
elif k >= a:
    b = b-(k-a)
    print(0,b)
else:
    a = a-k
    print(a,b)
