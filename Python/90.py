class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.results = []
        visited = [False] * len(nums)
        self.dfs(nums, visited, [], 0)
        return self.results
        
    def dfs(self, nums, visited, prev, start):
        self.results.append(prev)
        if start == len(nums):
            return 
        
        for i in range(start, len(nums)):
            if i > 0 and nums[i - 1] == nums[i] and not visited[i - 1]:
                continue
            visited[i] = True 
            self.dfs(nums, visited, prev + [nums[i]], i + 1)
            visited[i] = False
            
