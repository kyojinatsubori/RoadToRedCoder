k=int(input())
a,b=map(int,input().split())
ans=""
if a%k==0:
    ans="OK"
elif b-a>=k-a%k:
    ans="OK"
else:
    ans="NG"
print(ans)