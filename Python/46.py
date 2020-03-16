class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.results = []
        visited = [False] * len(nums)
        self.dfs(nums, [], visited)
        return self.results
    
    def dfs(self, nums, prev, visited):
        if len(prev) == len(nums):
            self.results.append(list(prev))
            return 
        
        for i in range(len(nums)):
            if visited[i]:
                continue
            prev.append(nums[i])
            visited[i] = True
            self.dfs(nums, prev, visited)
            visited[i] = False
            prev.pop()
        