#素因数分解
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

def judge(arr):
    for i in arr:
        if i[0]!=2 and i[0]!=3 and i[0]!=5:
            return False
    return True

n,d=map(int,input().split())
ans=0
x=[0,1,0,2,0,1]
y=[0,0,1,0,0,1]
z=[0,0,0,0,1,0]
#dを素因数分解する
sod=factorization(d)
#dの素因数に2,3,5以外が含まれていた場合、0を出力
if judge(sod):
    #dp法により確率計算を行う
    for i in range(n):
# dp[i][x][y][z]で考える
# x,y,zが各値の時、
# サイコロを振って条件を満たすパターン数を調べるよ。
print(ans)