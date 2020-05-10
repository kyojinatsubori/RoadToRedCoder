s=input()
t=input()
ans="UNRESTORABLE"
for i in range(len(s)-len(t),-1,-1):
    ss=s[i:i+len(t)]
    flag=0
    for j in range(len(t)):
        if ss[j]=="?":
            ss=ss[0:j]+t[j]+ss[j+1:]
        if ss[j]!=t[j]:
            flag=1
            break
    if flag==0:
        ans=s[0:i].replace("?","a")+ss+s[i+len(t):].replace("?","a")
        break
print(ans)