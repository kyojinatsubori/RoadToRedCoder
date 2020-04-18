from collections import Counter
Q = int(input())
s = ""
d = ""
for i in range(Q):
    n, c ,x = input().split()
    if n == "1":
        s = s + c*int(x)
    elif n == "2":
        sum = 0
        d = s[0:int(c):]
        s = s[int(c)::]
        counter = list(Counter(d).values())
        for i in counter:
            sum += i**2
        print(sum)


