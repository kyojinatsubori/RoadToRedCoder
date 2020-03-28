n, y = map(int, input().split())
a = 0
b = 0
c = 0
while y >= 10000:
    y -= 10000
    a += 1
while y >= 5000:
    y -= 5000
    b += 1
while y >= 1000:
    y -= 1000
    c += 1
else:
    n -= a + b + c
    while n > 0 and a >= 0:
        m = n
        bb = b
        cc = c
        while m > 0 and bb > 0:
            bb -= 1
            cc += 5
            m -= 4
        if m == 0:
            n = m
            b = bb
            c = cc
            break
        a -=1
        b += 2
        n -= 1
    if n != 0:
        a = -1
        b = -1
        c = -1
print (str(a)+" "+str(b)+" "+str(c))