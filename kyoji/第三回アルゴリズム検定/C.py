ans,r,n=map(int,input().split())
for i in range(1,n):
    ans*=r
    if ans>10**9:
        ans="large"
        break
print(ans)