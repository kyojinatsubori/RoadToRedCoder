A = input()
B = input()
C = input()
turn = "a"

for i in range(10**8):
    if turn == "a":
        if len(A) == 0:
            print("A")
            exit()
        else:
            turn = A[0]
            A = A[1::]
    elif turn == "b":
        if len(B) == 0:
            print("B")
            exit()
        else:
            turn = B[0]
            B = B[1::]
    else:
        if len(C) == 0:
            print("C")
            exit()
        else:
            turn = C[0]
            C = C[1::]