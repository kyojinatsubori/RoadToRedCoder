import decimal
a,b = map(str,input().split())
a = int(a)
b = int(decimal.Decimal(b)*100)
ab = (a*b)//100 
print(ab)
