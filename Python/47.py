class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, [], visited)
        return self.result
    
    
    def dfs(self, nums, cur, visited):
        if len(cur) == len(nums):
            self.result.append(cur)
            return 
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                continue 
            elif not visited[i]:
                visited[i] = True 
                self.dfs(nums, cur + [nums[i]], visited)
                visited[i] = False 
        return 
        
        