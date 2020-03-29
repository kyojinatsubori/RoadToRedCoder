s = input()
flag = 0
while len(s) > 0:
    if s[0:11] == "dreameraser":
        s = s[11:]
    elif s[0:10] == "dreamerase":
        s = s[10:]
    elif s[0:7] == "dreamer":
        s = s[7:]
    elif s[0:6] == "eraser":
        s = s[6:]
    elif s[0:5] == "dream":
        s = s[5:]
    elif s[0:5] == "erase":
        s = s[5:]
    else:
        flag =1
        break
if flag == 0:
    print("YES")
else:
    print("NO")