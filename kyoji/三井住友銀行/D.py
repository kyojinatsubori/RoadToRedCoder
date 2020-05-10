n=int(input())
s=input()
num=int(n*(n-1)*(n-2)/6)
ss=[]
for i in range(n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            ss.append(s[i]+s[j]+s[k])
sss=set(ss)
print(len(sss))