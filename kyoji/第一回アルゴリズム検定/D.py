n=int(input())
a=[0]*n
for i in range(n):
    a[int(input())-1]+=1
if 0 in a:
    print(str(a.index(2)+1)+" "+str(a.index(0)+1))
else:
    print("Correct")