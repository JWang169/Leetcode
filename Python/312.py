class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        f[i][j] = max{f[i][j] + a[i] * a[k] * a[j]}, i < k < j
        time: n^3, space: n^2  
        """
        n = len(nums) + 2
        balloons = [1] + nums + [1] # add 1 to head and tail 
        f = [[0] * n for _ in range(n)]
        
        for i in range(n - 1):
            f[i][i + 1] = 0  # balloon balloon
        
        for length in range(3, n + 1):
            # start position i: i + length <= n, i <= n - length
            # end position j:
            for i in range(n - length + 1):
                # end position
                j = i + length - 1 
                # k is the last balloono to burst between i and j
                for k in range(i + 1, j):
                    f[i][j] = max(f[i][j], f[i][k] + f[k][j] + balloons[i] * balloons[k] * balloons[j])
        
        
        return f[0][n - 1]
                    
                
        