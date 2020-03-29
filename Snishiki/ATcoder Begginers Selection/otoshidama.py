n, y = map(int, input().split())
answer = 0
a = 0
b = 0
c = 0

a = int(y / 10000)
if y % 10000 != 0:
    b = int(y % 10000 / 5000)
    if y % 10000 % 5000 != 0:
        c = int(y % 10000 % 5000 / 1000)
if a + b + c == n:
    print(str(a)+' '+str(b)+' '+str(c))
else :
    while a + b + c != n and a >= 0:
        d = b
        e = c
=======
        while a + d + e != n and d >= 1:
>>>>>>> fee5812b28ddf990824eb685c0337d1e2f2aa9d6
            d -= 1
            e += 5
        if a + d + e == n:
            b = d
            c = e
            break
        a -= 1
        b += 2
    if a + b + c == n:
        print(str(a)+' '+str(b)+' '+str(c))
    else :
        print('-1 -1 -1')