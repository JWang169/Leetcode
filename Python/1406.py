class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue) 
        # dp[i] means the highest score the current person can take over the next round  
        dp = [-sys.maxsize] * (n + 1)
        dp[-1] = 0
        for i in range(n - 1, -1, -1):
            cur = 0
            for k in range(3):
                # take 1/ 2/ 3
                if i + k < n:
                    cur += stoneValue[i + k]
                    dp[i] = max(dp[i], cur - dp[i + k + 1])
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        return "Tie"
                
    

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.seen = {}
        first = self.dfs(stoneValue)
        second = sum(stoneValue) - first
        if first > second:
            return "Alice"
        elif first < second:
            return "Bob"
        else:
            return "Tie"
    
    def dfs(self, nums):
        if not nums:
            return 0
        key = tuple(nums)
        if key in self.seen:
            return self.seen[key]
        
        if len(nums) == 1:
            self.seen[key] = nums[0]
            return self.seen[key]
        
        n = len(nums)
        if n > 2:
            cur = max(nums[0] + min(self.dfs(nums[2:]), self.dfs(nums[3:]), self.dfs(nums[4:])),
                 nums[0] + nums[1] + min(self.dfs(nums[3:]), self.dfs(nums[4:]), self.dfs(nums[5:])),
                 nums[0] + nums[1] + nums[2] + min(self.dfs(nums[4:]), self.dfs(nums[5:]), self.dfs(nums[6:])))
        else:
            cur = max(nums[0] + min(self.dfs(nums[2:]), self.dfs(nums[3:]), self.dfs(nums[4:])),
                 nums[0] + nums[1] + min(self.dfs(nums[3:]), self.dfs(nums[4:]), self.dfs(nums[5:])))
        self.seen[key] = cur
        return cur 
                 
                                         
        
        