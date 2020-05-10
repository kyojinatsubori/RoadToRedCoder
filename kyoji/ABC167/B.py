a,b,c,k=map(int,input().split())
if a<k:
    if b<k-a:
        ans=a+(k-a-b)*(-1)
    else:
        ans=a
else:
    ans=k
print(ans)