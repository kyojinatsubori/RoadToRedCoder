s=input()
words=[]
flag=0
memo=0
for i in range(0,len(s)):
    if s[i].isupper():
        if flag==0:
            flag=1
            memo=i
        else:
            flag=0
            words.append(s[memo:i+1])
words = sorted(words, key=str.lower)
print("".join(words))