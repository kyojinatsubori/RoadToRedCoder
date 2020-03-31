from collections import deque
n = int(input())
dick = {}
for i in range(n):
    dick.setdefault(map(int,input().split()))
    print(dick.items())