n,k,c=map(int, input().split())
s=input()
L=[0]*k
R=[0]*k
m=0
l=0
for i in range(k):
    while s[m]=="x":
        m+=1
    L[i]=m
    m+=c+1
    while s[n-l-1]=="x":
        l+=1
    R[i]=n-l-1
    l+=c+1
for i in range(k):
    if R[k-i-1]==L[i]:
        print(L[i]+1)