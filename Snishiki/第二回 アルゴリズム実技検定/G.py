from collections import Counter
Q = int(input())
s = ""
d = ""
for i in range(Q):
    Query = list(input().split())
    if Query[0] == "1":
        s = s + Query[1]*int(Query[2])
    elif Query[0] == "2":
        sum = 0
        d = s[0:int(Query[1]):]
        s = s[int(Query[1])::]
        counter = list(Counter(d).values())
        for i in counter:
            sum += i**2
        print(sum)


