import sys
s = input()
for i in range(len(s)//2):
    if s[i] != s[len(s) - i - 1]:
        print("No")
        sys.exit(0)
for i in range((len(s) - 1)//4):
    if s[i] != s[(len(s) - 1)//2 - i - 1]:
        print("No")
        sys.exit(0)
print("Yes")

#s=input();print('YNeos'[s.count(s[:len(s)//2])<2::2])