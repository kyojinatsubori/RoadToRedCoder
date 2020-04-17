s = input()
end = (len(s)-1)//2
start = (len(s)+3)//2
if s[0:end] == s[end-1::-1]:
    if s[start-1::] == s[-1:start-2:-1]:
        if s[0::] == s[::-1]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")