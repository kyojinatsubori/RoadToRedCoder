N,M = map(int,input().split())
a = list(map(int,input().split()))
child = [0]*N

def bisect_right_reverse(a, x):
    '''
    reverseにソートされたlist aに対してxを挿入できるidxを返す。
    xが存在する場合には一番右側のidx+1となる。
    '''
    if a[0] < x:
        return 0
    if x <= a[-1]:
        return len(a)
    # 二分探索
    ok = len(a) - 1
    ng = 0
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if a[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok

for i in a:
    ind = bisect_right_reverse(child, i)
    if ind == N:
        print(-1)
    else:
        child[ind] = i
        print(ind+1)