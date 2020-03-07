def findMax(times, deadlines, profits):
	n = deadlines[-1] + 1
	m = len(deadlines)
	f = [[0] * n for _ in range(m)]
	for j in range(n):
		if j < deadlines[0]:
			continue
		f[0][j] = profits[0]

	for i in range(1, m):
		for j in range(n):
			f[i][j] = f[i - 1][j]
			if j - times[i] >= 0:
				f[i][j] = max(f[i - 1][j], profits[i] + f[i][j - times[i]])
	print(f)
	return f[-1][-1]

times = [5, 8, 5, 2]
deadlines = [5, 9, 10, 12]
profits = [3,4,2, 5]

res = findMax(times, deadlines, profits)
print(res)
