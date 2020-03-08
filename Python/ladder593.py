import sys 
class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def stoneGame2(self, A):
    # circle 你就懵逼了
    # 复制一份数组接在原来的数组后面
    # 找下标范围len(A)的和最小值
        n = len(A)
        if n <= 1:
            return 0
        
        B = A + A  # double size list  
        dp = [[0] * 2 * n for _ in range(2 * n) ]
        
        # still go through all length
        for length in range(2, n + 1):
            for i in range(2 * n - length + 1):        # starting point
                j = i + length - 1 
                dp[i][j] = sys.maxsize
                score = self.getScore(i, j, B)
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + score)
        res = sys.maxsize
        for i in range(n):
            res = min(dp[i][i+n-1], res)
            
        return res 
                
                
    def getScore(self, i, j, B):
        return sum(B[i : j + 1])
                