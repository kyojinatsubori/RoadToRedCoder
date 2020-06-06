N = int(input())
ans = ""
hour = N//3600
if hour <= 9:
    ans += "0"
ans += str(hour)+":"
temp = N%3600
minute = temp//60
if minute <= 9:
    ans += "0"
ans += str(minute)+":"
second = temp%60
if second <= 9:
    ans += "0"
ans += str(second)

print(ans)