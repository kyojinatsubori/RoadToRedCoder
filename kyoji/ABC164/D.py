s=input()
ls=len(s)
count=0
for i in range(ls-4):
    for j in range(i+5,ls+1):
        if int(s[i:j])%2019==0:
            count+=1
print(count)