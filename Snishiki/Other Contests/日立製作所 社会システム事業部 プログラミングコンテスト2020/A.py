s = input()
while s[0:2:] == "hi":
    s = s[2::]
if len(s) == 0:
    print("Yes")
else:
    print("No")