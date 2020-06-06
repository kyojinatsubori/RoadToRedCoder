S = input()

for i in range(3):
    if not S[i].isdigit():
        print("error")
        exit()
S = int(S)
print(S*2)