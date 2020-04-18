S,T = map(str,input().split())
if S[0] == "B" and T[0]=="B":
    print(abs(int(S[1])-int(T[1])))
elif S[1] =="F" and T[1] =="F":
    print(abs(int(S[0])-int(T[0])))
elif S[1] =="F" and T[0] =="B":
    print(int(T[1])+int(S[0])-1)
else:
    print(int(S[1])+int(T[0])-1)
