n,m=map(int,input().split())
a=list(map(int,input().split()))
if n-sum(a)<0:
    print("-1")
else:
    print(n-sum(a))