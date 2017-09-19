'''
n = months
k = number of rabbit pairs that are produced with each rabbit pairs
'''
n = 30
k = 5
a = 1
for month in range(n):
	a, k = k, a+k
print(a+1)