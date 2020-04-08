class Solution:
    def numTrees(self, n: int) -> int:
        # dp[i] 代表i个节点的二叉树
        dp = [0] * (n + 1)
        dp[0] = 1 
        dp[1] = 1
        # i是总的节点数，从2到n
        for i in range(2, n + 1):
            # 当root 是 i 的时候，左子树小于root，所以左子树(j)从0到i-1
            for j in range(i):
                # 一共i个节点，左子树占j个，根节点1个，右子树还剩i - j - 1个
                dp[i] += dp[j] * dp[i - j - 1]
        return dp[-1]
        


class Solution:
    def numTrees(self, n: int) -> int:
        self.seen = dict()
        self.seen[0] = 1 
        self.seen[1] = 1
        return self.dfs(n)
    
    
    def dfs(self, n):
        if n in self.seen:
            return self.seen[n]
        cur = 0
        for i in range(1, n + 1):
            cur += self.dfs(i - 1) * self.dfs(n - i)
        
        self.seen[n] = cur
        return cur 