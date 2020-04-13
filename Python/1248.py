class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        odd_count = 0
        nice_count = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 1:
                odd_count += 1 
                count = 0
            
            while odd_count == k:
                # if nums[left] is odd, update odd_count 
                odd_count -= nums[left] % 2
                left += 1 
                count += 1 
            nice_count += count
                
        return nice_count
        
        