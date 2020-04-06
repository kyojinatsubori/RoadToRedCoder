from collections import deque
k = int(input())
que = deque([1,2,3,4,5,6,7,8,9])
for i in range(k):
    ans=que.popleft()
    if ans%10!=0:
        que.append(10*ans+ans%10-1)
    que.append(10*ans+ans%10)
    if ans%10!=9:
        que.append(10*ans+ans%10+1)
print(ans)
