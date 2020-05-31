N = int(input())
s = [0]* N
Middle = 0
Bcount = 0
Acount = 0
ABcount = 0
ans = 0
for i in range(N):
    s[i] = input()
    if s[i][0] == "B" and s[i][-1] == "A":
        ABcount += 1
    elif s[i][0] == "B":
        Bcount += 1
    elif s[i][-1] == "A":
        Acount += 1
    for j in range(len(s[i])-1):
        if s[i][j] == "A" and s[i][j+1] == "B":
            Middle += 1
if ABcount==0 and Acount==0 and Bcount==0:
    ans = Middle
elif Acount == 0 and Bcount==0:
    ans = Middle + ABcount - 1
elif Acount == 0:
    ans = Middle + ABcount
elif Bcount == 0:
    ans = Middle + ABcount
else:
    ans = Middle + ABcount +1 + min(Acount-1,Bcount-1)
print(ans)



    