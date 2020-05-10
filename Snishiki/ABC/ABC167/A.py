S = input()
T = input()
if S == T[0:len(T)-1:] and T[-1].islower():
    print("Yes")
else:
    print("No")