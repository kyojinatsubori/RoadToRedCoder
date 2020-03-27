a = int(input())
b = int(input())
c = int(input())
x = int(input())
maxA = 0 #最大限500円を使う時の枚数
maxB = 0 #更に最大限100円を使う時の枚数
while x >= 500 and a >= 1:
    x -= 500
    a -= 1
    maxA += 1
while x >= 100 and b >= 1:
    x -=100
    b -= 1
    maxB +=1
if x % 50 == 0:
    maxC = x / 50 #その時50円を使う枚数
else:
    maxC = 0

countA = 0#500円⇒100円の回数
countB = 0#100円⇒50円の回数
countC = 0#500円⇒50円の回数

while maxA > 0 and b - maxB >= 5:
    maxA -= 1
    maxB += 5
    countA += 1
    while maxB > 0 and c - maxC >= 2:
        maxB -= 1
        maxC += 2
        countB += 1
while maxA > 0 and c - maxC >= 10:
    maxA -= 1
    maxC += 10
    countC += 1
while maxB > 0 and c - maxC >= 2:
    maxB -= 1
    maxC += 2
    countC += 1
print(countA + countB + countC)