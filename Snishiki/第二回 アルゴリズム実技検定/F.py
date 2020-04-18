n=int(input())
ab=[0]*n
for i in range(n):
    ab[i]=list(map(int,input().split()))
ab.sort(key=lambda x: x[0])
sum=0
lab=[]
for k in range(1,n+1):
    #abの中でAiがkのものを足す
    pin=[i for i in ab if ab[i][0]==k]
    lab.extend(pin)
    #その中でBiが最大の物を選択し、sumに足す
    max_lab=max(lab)

    #abから選んだものを取り除く
    #sumを出力する