class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.results = []
        candidates.sort()
        visited = [False] * len(candidates)
        self.dfs(candidates, 0, [], target, visited)
        return self.results
        
    def dfs(self, candidates, start, prev, target, visited):
        if target == 0:
            self.results.append(list(prev))
            return 
        if target < 0:
            return 
        
        for i in range(start, len(candidates)):
            if i > 0 and candidates[i] == candidates[i - 1] and not visited[i - 1]:
                continue   
            # add current number
            visited[i] = True
            self.dfs(candidates, i + 1, prev + [candidates[i]], target - candidates[i], visited)
            visited[i] = False
        return 