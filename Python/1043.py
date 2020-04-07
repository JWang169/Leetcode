# April 6 自己写过了 debug了几遍 return dp[n-1] 很tricky
class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp = [0] * (n + 1) 
        for i in range(n):    
            ma = 0
            for j in range(K):
                if i - j < 0:
                    break
                ma = max(ma, A[i - j])
                dp[i] = max(dp[i], dp[i - j - 1] + ma * (j + 1))
        return dp[n - 1]
        
        

class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A or len(A) == 0:
            return 0
        n = len(A)
        dp = [0] * (n + 1)
        for i in range(n):
            curMax = A[i]
            for j in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i- j + 1])
                dp[i] = max(dp[i], dp[i - j] + curMax * j)
        return dp[n - 1]