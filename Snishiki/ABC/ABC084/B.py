import re
A, B = map(str,input().split())
S = input()
pattern = r'[0-9]{'+A+'}-[0-9]{'+B+'}'
matchObj = re.match(pattern, S)
if matchObj:
    print("Yes")
else:
    print("No")

