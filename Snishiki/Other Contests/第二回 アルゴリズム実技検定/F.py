n=int(input())
ab=[0]*n
for i in range(n):
    ab[i]=list(map(int,input().split()))
ab.sort(key=lambda x: x[0])
sum=0
lab=[]
for k in range(1,n+1):
    #abの中でAiがkのものを足す
    if len(ab) != 0:
        while ab[0][0]<=k:
            lab.append(ab[0][1])
            ab.pop(0)
            if len(ab) == 0:
                break
    #その中でBiが最大の物を選択し、sumに足す
    max_lab=max(lab)
    sum += max_lab
    #labから選んだものを取り除く
    lab.pop(lab.index(max_lab))
    #sumを出力する
    print(sum)