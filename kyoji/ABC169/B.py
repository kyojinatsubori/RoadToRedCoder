n=int(input())
array=list(map(int,input().split()))
ans=array[0]
for i in range(1,n):
    ans*=array[i]
    if ans>10**18:
        ans=-1
        break
if 0 in array:
    ans=0
print(ans)