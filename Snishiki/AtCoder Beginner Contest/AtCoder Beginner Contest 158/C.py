import math
A,B = map(int, input().split())
answerA = math.ceil(A/0.08)
answerAA = math.ceil((A+1)/0.08 -1)
answerB = math.ceil(B/0.1)
answerBB = math.ceil((B+1)/0.1 -1)
if answerA == answerAA:
    if answerA >= answerB and answerA <= answerBB:
        print(answerA)
elif answerB == answerBB:
    if answerB >= answerA and answerB <= answerAA:
        print(answerB)
else:
    if answerB > answerAA:
        print("-1")
    elif answerB == answerAA:
        print(answerAA)
    elif answerA < answerB and answerAA > answerB:
        print(answerB)
    elif answerA == answerB:
        print(answerB)
    elif answerB < answerA and answerBB >= answerA:
        print(answerA)
    elif answerBB < answerA:
        print("-1")
    else:
        print("-1")
