class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        cumsum = 0
        left = 0
        result = sys.maxsize
        for i in range(len(nums)):
            cumsum += nums[i]
            if cumsum < s:
                continue 
            
            result = min(result, i - left + 1)
            while cumsum >= s:
                result = min(result, i - left + 1)
                cumsum -= nums[left]
                left += 1 

        
        return result if result < sys.maxsize else 0
            
            
        