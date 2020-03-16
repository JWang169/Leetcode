class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        self.dfs(nums, 0, [])
        return self.results
    
    def dfs(self, nums, start, prev):
        self.results.append(list(prev))
        if start == len(nums):
            return 
        
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, list(prev + [nums[i]]))
            
        