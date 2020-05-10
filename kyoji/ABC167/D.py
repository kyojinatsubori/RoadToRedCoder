import math
def binary_search(list,target):

	result = -1
	left = 0
	right = len(list) - 1

	while left <= right:
		center = int((left + right)/2)
		if list[center] == target:
			result = center
			break
		elif list[center] < target:
			left = center + 1
		elif list[center] > target:
			right = center - 1

	if result == -1:
		return False
	else:
		return True

n,k=map(int,input().split())
a=list(map(int,input().split()))
i=0
pasta=[1]
while True:
    if binary_search(pasta,a[i]):
        roopy=pasta.index(a[i])
        roop=pasta[roopy:]
        break
    else:
        pasta.append(a[i])
        i=a[i]-1
if k>len(pasta):
    k-=len(pasta)
    k%=len(roop)
    print(roop[k])
else:
    print(pasta[k])