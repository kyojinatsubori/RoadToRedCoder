N = int(input())
S = []
for i in range(5):
    S.append(input())
ans = []
for i in range(1, N+1):
    first = 4*i-3
    second = 4*i-2
    third = 4*i-1
    if S[0][first] == "#":
        if S[0][second] == "#":
            if S[4][first] == "#":
                if S[2][second] == "#":
                    if S[1][first] == "#":
                        if S[3][first] == "#":
                            if S[1][third] == "#":
                                ans.append("8")
                            else:
                                ans.append("6")
                        else:
                            if S[1][third] == "#":
                                ans.append("9")
                            else:
                                ans.append("5")
                    else:
                        if S[3][first] == "#":
                            ans.append("2")
                        else:
                            ans.append("3")
                else:
                    ans.append("0")
            else:
                ans.append("7")
        else:
            ans.append("4")
    else:
        ans.append("1")
print("".join(ans))
