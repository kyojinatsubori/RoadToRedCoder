s = int(input())
a = 0
b = 0
a = s // 500
b = s % 500 // 5
print(1000 * a + 5 * b)