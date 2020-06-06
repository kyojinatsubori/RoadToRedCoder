N = int(input())
kuku = 2025
sa = kuku - N

for i in range(1,10):
    if sa % i == 0 and sa//i <= 9:
        print(str(i) + " x " + str(sa//i))

