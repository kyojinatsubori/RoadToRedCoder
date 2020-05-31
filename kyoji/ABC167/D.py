n,k=map(int,input().split())
a=list(map(int,input().split()))
i=0
pasta=[1]
memo=[0]*n
while True:
    if memo[a[i]-1]>0:
        roopy=pasta.index(a[i])
        roop=pasta[roopy:]
        break
    else:
        memo[a[i]-1]+=1
        pasta.append(a[i])
        i=a[i]-1
if k>len(pasta):
    k-=len(pasta)
    k%=len(roop)
    print(roop[k])
else:
    print(pasta[k])