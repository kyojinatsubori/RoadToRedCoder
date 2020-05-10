x=int(input())
n=100
count=0
while n<x:
    n+=int(n*0.01)
    count+=1
print(count)