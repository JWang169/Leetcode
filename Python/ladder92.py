class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @return: The maximum size
    """
    def backPack(self, m, A):
        # 背包问题一定用最大总承重当成其中一维
        n = len(A)
        f = [[False] * (m + 1) for _ in range (n + 1)]
        
        f[0][0] = True 
        for i in range(1, m):  # 用数组里前0个数，能否组成i（i的范围就是从0到m） 
            f[0][i] = False  # 所以只有f[0][0]是true，其他都是false
                 
        for i in range(1, n + 1):
            f[i][0] = True
            for j in range(1, m + 1):
                # if A[i - 1] > j: # 当前物品重量大于总重：false
                #     f[i][j] = False
                #     continue 
                if A[i - 1] <= j:
                    f[i][j] = f[i - 1][j - A[i - 1]] or f[i - 1][j]
                else:
                    f[i][j] = f[i - 1][j]
        idx = m
        while idx > 0:
            if f[n][idx] == True:
                return idx 
            idx -= 1 
        return idx 
                    