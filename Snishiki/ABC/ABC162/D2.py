N = int(input())
S = input()
count = 0
R = S.count("R")
G = S.count("G")
B = S.count("B")
count = R*G*B

for i in range(N-2):
    for j in range(i+1, N-1):
        if j +(j-i) <= N-1 and S[i] != S[j]:
            if S[i] != S[j+(j-i)] and S[j] != S[j+(j-i)]:
                count -= 1

print(count)