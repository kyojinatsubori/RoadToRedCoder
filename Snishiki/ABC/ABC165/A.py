K = int(input())
A,B = map(int,input().split())

if A % K == 0:
    print("OK")
else:
    if K - (A % K) <= B - A:
        print("OK")
    else:
        print("NG") 