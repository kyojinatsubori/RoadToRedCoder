s=input()
t=input()
ans='No'
if len(s)+1==len(t):
    if s==t[0:len(t)-1]:
        ans='Yes'
print(ans)