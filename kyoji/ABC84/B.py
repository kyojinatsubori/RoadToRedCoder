a,b=map(int,input().split())
s=input()
mae=s[0:a]
ushiro=s[a+1:]
if mae.isdigit() and ushiro.isdigit() and s[a]=='-':
    print('Yes')
else:
    print('No')
