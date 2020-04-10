import math
n=int(input())
s=input()
if n%2==0 and s[0:int(n/2)]+s[0:int(n/2)]==s:
    print("Yes")
else:
    print("No")