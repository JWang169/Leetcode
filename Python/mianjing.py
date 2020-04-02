"""
第一轮
给一个 m*n 的空矩阵，有一个 API 可以每天随机加一个 tower (矩阵里面的一个点)。一个 tower 代表矩阵里的一个点
相邻（上下左右）的 tower之间可以连通。
问多少天能连通最左最右两个 column (任意 column 上面的点就行)。 相当于就是问什么时候可以确定最左最右是连通的
"""

def tower(grid, x, y):
	m, n = len(grid[0]), len(grid)
	dx = [-1, 1, 0, 0]
	dy = [0, 0, -1, 1]
	for i in range(4):
		nx, ny = x + dx[i] + y + dy[i]
		if 0 <= nx < m and 0 <= ny < n:
			if grid[nx][ny] == 1:
				self.connection[(nx, ny)] = (x, y)
	return self.find(x, y)


def find(x, y):
	left, right = False, False 
	while self.connection[(x, y)] != (x, y):
		if y == 0:
			left = True 
		if y == n - 1:
			right = True
		(x, y) = self.connections[(x, y)]

	if left and right:
		return True 
	return False 


"""
第二轮
有一个 graph （其实是 tree），每个node 代表一个 castle，edge 是 castle 之间的连接，edge 代表 castle 之间传递信息需要的时间
问题就是给定一个起点，问需要多少时间能传遍所有的 castle
follow up: 怎么按照信息到达 castle 的时间输出 castle 的 id
"""

# NETWORD DELAY

"""
第三轮
给一个 array，求 array 里面最短的 subarry，使得 array 里面 element 的和等于 K
"""
	




