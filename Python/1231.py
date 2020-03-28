class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        left, right = 0, sum(sweetness)
        while left + 1 < right:
            mid = (left + right) // 2 
            count = self.search(sweetness, mid)
            if count >= K + 1:
                left = mid 
            else:
                right = mid 
        
        count = self.search(sweetness, right)
        if count == K + 1:
            return right
        return left
        
        
    def search(self, sweetness, mid):
        count = 0
        cur = 0
        for sweet in sweetness:
            cur += sweet
            if cur >= mid:
                count += 1
                cur = 0
        return count
        
        
#         if not sweetness or len(sweetness) < K:
#             return 0
#         self.result = 0
#         self.dfs(sweetness, K + 1, sys.maxsize)
#         return self.result
        
    
#     def dfs(self, sweetness, k, mini):
#         if k == 0:
#             self.result = max(self.result, mini)
#             return 
        
#         if len(sweetness) == k:
#             curResult = min(min(sweetness), mini)
#             self.result = max(curResult, self.result)
#             return 
        
#         curSweet = 0
#         for i in range(len(sweetness) - k + 1):
#             curSweet += sweetness[i]
#             newMini = min(mini, curSweet)
#             self.dfs(sweetness[i + 1:], k - 1, newMini)
            
            
            
            
            
            