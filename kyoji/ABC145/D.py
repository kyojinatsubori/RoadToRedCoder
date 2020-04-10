import math
def combi(n, m):
    val = m
    for i in range(m+1, n+1):
        val *= i
        while val>=10**9+7:
            val-=10**9+7
    mal=1
    for i in range(2, m+1):
        mal *= i
        while mal>=10**9+7:
            mal-=10**9+7
    val//=mal
    return val

x, y=map(int,input().split())
if (2*y-x)%3==0:
    a=int((2*y-x)/3)
    b=int((2*x-y)/3)
    c=a+b
    print(combi(c,a))
else:
    print("0")