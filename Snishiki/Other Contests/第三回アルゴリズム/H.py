n,l=map(int,input().split())
x=list(map(int,input().split()))
x=set(x)
t1,t2,t3=map(int,input().split())
dp=[float('inf')]*(l+4)
dp[0]=0
route1=float('inf')
route2=float('inf')
route3=float('inf')
for i in range(1,l+4):
    route1=dp[i-1]+t1
    if i-1 in x:
        route1+=t3
    if i>=2:
        route2=dp[i-2]+t1+t2
        if i-2 in x:
            route2+=t3
    if i>=4:
        route3=dp[i-4]+t1+t2*3
        if i-4 in x:
            route3+=t3
    dp[i]=min(route1,route2,route3)
ans=[]
ans.append(dp[l])
for i in range(max(l-3,0),l):
    kouho1=dp[i]+t1*0.5+t2*(l-i-0.5)
    if i in x:
        kouho1+=t3
    ans.append(int(kouho1))
print(min(ans))