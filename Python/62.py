class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m <= 1 or n <= 1:
            return 1
        prev = [1] * n
        
        for i in range(1, m):
            cur = [0] * n
            for j in range(n):
                if j == 0:
                    cur[j] = prev[j]
                    continue
                cur[j] = cur[j - 1] + prev[j]
            prev = cur
        
        return prev[-1]