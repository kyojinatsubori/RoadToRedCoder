N = int(input())

for i in range(1, 10**6):
    if i**2 > N:
        print((i-1)**2)
        exit()
    