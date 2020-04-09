# 我可能是真的会了 April 8th
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.seen = {}
        first = self.dfs(nums)
        total = sum(nums)
        return first >= total - first 
        
    def dfs(self, nums):
        if not nums:
            return 0
        key = tuple(nums)
        if key in self.seen:
            return self.seen[key]
        
        if len(nums) == 1:
            self.seen[key] = nums[0]
            return nums[0]
        
        total = sum(nums)
        
        cur = total - min(self.dfs(nums[1:]), self.dfs(nums[:len(nums) - 1]))
        self.seen[key] = cur
        return cur
        

# 这个就是把recursive的方法翻译过来了
class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # dp[][]的方法
        if not nums:
            return True 
        
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        # 如果只有一个可选
        for i in range(n):
            dp[i][i] = nums[i]
        
        # dp[i][j]表示现在这堆数是nums[i: j]， 要么选nums[j], 要么选nums[i]，能获得的最大sum是多少 
        #                选nums[i]    对手选nums[i + 1]或者nums[j]         选nums[j]      对手选nums[i]   或者nums[j - 1]
        # dp[i][j] = max(nums[i] + min(dp[i + 2][j], dp[i + 1][j - 1])， nums[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
        # 这就是为什么要从length (k) 开始loop 
        for k in range(2, n + 1):
            for i in range(n - k, -1, -1):
                j = i + k - 1
                a = dp[i + 2][j] if i + 2 < n else 0
                b = dp[i][j - 2] if j - 2 >= 0 else 0
                c = dp[i + 1][j - 1] if i + 1 < n and j - 1 >= 0 else 0
                dp[i][j] = max(nums[i] + min(c, a), nums[j] + min(c, b))
        print(dp)
        return dp[0][n - 1] * 2 >= sum(nums)
        
        
        

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.seen = {}
        first = self.dfs(nums)
        return first >= sum(nums) - first
    
    def dfs(self, nums):
        if not nums:
            return 0
        key = tuple(nums)
        
        if key in self.seen:
            return self.seen[key]
        
        if len(nums) == 1:
            self.seen[key] = nums[0]
            return self.seen[key]
        
        # if pick from the front, the other person will do the optimal way. 
        # and next time I will choose the max from the min
        n = len(nums)
        cur = max(nums[0] + min(self.dfs(nums[2:]), self.dfs(nums[1: n - 1])), 
                  nums[-1] + min(self.dfs(nums[1: n-1]), self.dfs(nums[:n - 2])))
        self.seen[key] = cur
        return cur
            
        
        
        