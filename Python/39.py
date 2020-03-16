class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        self.dfs(candidates, 0, [], 0, target)
        return self.results
    
    def dfs(self, candidates, start, prev, cumsum, target):
        if cumsum == target:
            self.results.append(list(prev))
            return 
        if cumsum > target:
            return 
        
        for i in range(start, len(candidates)):
            self.dfs(candidates, i, prev + [candidates[i]], cumsum + candidates[i], target)
            
    