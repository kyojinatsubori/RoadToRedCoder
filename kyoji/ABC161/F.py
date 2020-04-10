def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
import fractions
a = list(map(int, input().split()))
ant = a[0]
for i in range(1, N):
    ant = fractions.gcd(ans, a[i])

print(ans)
N=int(input())
array=factorization(N)
print(array)
ans=2
for i in array:
    M=N/(i[0]**i[1])
    if M%i[0]==1:
        ans+=1
        factorization(i[1])[]
print(ans)
#途中。k**mの複数の表し方が可能な場合が漏れている。