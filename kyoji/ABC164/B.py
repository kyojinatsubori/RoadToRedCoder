a,b,c,d=map(int,input().split())
flag=""
while a>0 and c>0:
    c-=b
    if c<=0:
        flag="Yes"
        break
    a-=d
    if a<=0:
        flag="No"
        break
print(flag)