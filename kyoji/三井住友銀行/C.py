x=int(input())
a=x//100
b=x%100
if b>=0 and b<=5*a:
    print("1")
else:
    print("0")