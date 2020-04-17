s = input()

while True:
    if len(s) != 0:
        if s[:5:] == "erase":
            s = s[5::]
            if s[0:1:] == "r":
                s = s[1::]
        elif s[:5:] == "dream":
            s = s[5::]
            if s[0:3:1] == "ere" or s[0:3:1] == "erd":
                s = s[2::]
            elif s == "er":
                print("YES")
                break
        else:
            print("NO")
            break
    else:
        print("YES")
        break