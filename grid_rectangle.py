n, m = map(int, input().split())

for i in range(n):
	for j in range(m):
		if (i + j) % 2 == 0:
			print('B', end='')
		else:
			print('W', end='')
	print()