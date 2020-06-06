N,Q = map(int,input().split())
table = [0]*N
con = [0]*N
for i in range(N):
    table[i] = i
    con[i] = i
print(table)
print(con)