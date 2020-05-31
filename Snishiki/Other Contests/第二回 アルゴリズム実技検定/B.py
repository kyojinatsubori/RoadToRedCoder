s=input()
an=s.count("a")
ans="a"
if an<s.count("b"):
    ans="b"
    an=s.count("b")
if an<s.count("c"):
    ans="c"
print(ans)
