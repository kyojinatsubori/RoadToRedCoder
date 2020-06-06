S = input()
words = []
memo = 0
flag = 0
for i in range(len(S)):
    if S[i].isupper():
        if flag == 0:
            memo = i
            flag = 1
        else:
            words.append(S[memo:i+1])
            flag = 0
words = sorted(words, key=str.lower)
print("".join(words))
