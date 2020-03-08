class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        f = [[0] * (m + 1) for _ in range(len(A) + 1)]
        
        for i in range(1, len(A) + 1):
            for j in range(1, m + 1):
                f[i][j] = f[i - 1][j]
                if j - A[i - 1] >= 0:
                    f[i][j] = max(f[i][j], f[i - 1][j - A[i - 1]] + V[i - 1])
                
        return max(f[len(A)])
                