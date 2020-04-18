n=int(input())
s=[0]*n
for i in range(n):
    s[i]=list(input())
for i in range(n-2,-1,-1):
    for j in range(1,2*n-2):
        if s[i][j]=="#"and(s[i+1][j-1]=="X" or s[i+1][j]=="X" or s[i+1][j+1]=="X"):
                s[i][j]="X"
for i in s:
    print("".join(i))