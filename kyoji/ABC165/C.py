n,m,q=map(int,input().split())
abcd=[0]*q
for i in range(q):
    abcd[i]=list(map(int,input().split()))
abcd=sorted(abcd,key=lambda x:x[0])
print(abcd)
