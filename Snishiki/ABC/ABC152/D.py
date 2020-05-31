N = input()
l = len(N)
if l == 1:
    print(N)
    exit()
nf = N[0]
ne = N[-1]
nm = 0
base = 1
if l > 2:
    nm = int(N[1:l-1:])
for i in range(1,l-2):
    base += 10**i
ans = 0

for i in range(int(N)+1):
    i = str(i)
    f = i[0]
    e = i[-1]
    if e != "0":
        if f == e:
            ans += 1
        if e < nf:
            ans += base
            if l > 2:
                ans += 10**(l-2)
        elif e == nf:
            if f <= ne:
                ans += base
                if l>2:
                    ans += nm + 1
            else:
                ans += base
                ans += nm
        else:
            if l >2:
                ans += base
print(ans)



