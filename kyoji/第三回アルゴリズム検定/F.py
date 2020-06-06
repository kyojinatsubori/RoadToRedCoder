n=int(input())
s=["" for _ in range(n)]
for i in range(n):
    s[i]=input()
flag=0
ans=""
if n%2==0:
    for i in range(int(n/2)-1,-1,-1):
        both=list(set(s[i]) & set(s[n-i-1]))
        if len(both)==0:
            ans=-1
            break
        else:
            ans=both[0]+ans+both[0]
else:
    ans=s[int((n-1)/2)][0]
    for i in range(int((n-1)/2)-1,-1,-1):
        both=list(set(s[i]) & set(s[n-i-1]))
        if len(both)==0:
            ans=-1
            break
        else:
            ans=both[0]+ans+both[0]
print(ans)