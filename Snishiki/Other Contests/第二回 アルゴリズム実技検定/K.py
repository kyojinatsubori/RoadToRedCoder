n=int(input())
s=input()
c=list(map(int,input().split()))
d=list(map(int,input().split()))
left_sum=0
right_sum=0
sum=0
lefts_c=[]
lefts_d=[]
for i in range(n):
    if s[i]=="(":
        left_sum+=1
    else:
        right_sum+=1
    if left_sum-right_sum<0:#この時の分岐を再考する必要あり！
        sum+=min(c[i],d[i])
        left_sum+=1
        right_sum-=1
    elif left_sum-right_sum==0:
        left_sum=0
        right_sum=0
        lefts_c=[]
        lefts_d=[]
    else:
        lefts_c.append(i)
        lefts_d.append(i)
while left_sum-right_sum>0:
    left_sum-=1
    sum+=min(min(lefts_c),min(lefts_d))
    if min(lefts_c)>min(lefts_d):
        i=lefts_d.index(min(lefts_d))
        lefts_c.pop(i)
        lefts_d.pop(i)
    else:
        i=lefts_c.index(min(lefts_c))
        lefts_c.pop(i)
        lefts_d.pop(i)
print(sum)