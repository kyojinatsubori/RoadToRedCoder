import collections

N = int(input())
S = [0]*N
for i in range(N):
    S[i] = input()
c = collections.Counter(S)

print(len(c.most_common()))