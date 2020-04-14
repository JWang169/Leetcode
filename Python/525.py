class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones = {0: 0}
        countOne = 0
        result = 0
        
        for i, n in enumerate(nums):
            i = i + 1
            if n == 1:
                countOne += 1 
            else:
                countOne -= 1 
                
            if countOne in ones:
                result = max(result, i - ones[countOne])
            else:
                ones[countOne] = i
        return result
            
        
        