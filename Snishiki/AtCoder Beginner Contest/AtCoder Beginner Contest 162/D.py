N = int(input())
S = input()
count = 0

for i in range(N-2):
    for j in range(i+1, N-1):
        if S[i] != S[j]:
            for k in range(j+1, N):
                if j - i != k - j and S[i] != S[k] and S[j] != S[k]:
                    count += 1

print(count)
