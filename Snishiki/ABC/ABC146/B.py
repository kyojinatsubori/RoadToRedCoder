N = int(input())
S = input()
ans = ""
l = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in range(len(S)):
    index = l.index(S[i])
    if index + N >= 26:
        ans += l[index+N-26]
    else:
        ans += l[index+N]
print(ans)