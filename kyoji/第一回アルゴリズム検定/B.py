n=int(input())
a=[0]*n
a[0]=int(input())
for i in range(1,n):
    a[i]=int(input())
    if a[i]==a[i-1]:
        print("stay")
    elif a[i]<a[i-1]:
        print("down "+str(a[i-1]-a[i]))
    else:
        print("up "+str(a[i]-a[i-1]))