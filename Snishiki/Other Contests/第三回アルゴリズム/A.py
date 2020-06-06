s=input()
t=input()
ans="different"
if s[0]==t[0] and s[1]==t[1] and s[2]==t[2]:
    ans="same"
elif s[0].upper()==t[0].upper() and s[1].upper()==t[1].upper() and s[2].upper()==t[2].upper():
    ans="case-insensitive"
print(ans)