class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """
    def deduplication(self, nums):
        seen = set()
        pointer = 0
        for idx, num in enumerate(nums):
            if num not in seen:
                seen.add(num)
                nums[pointer], nums[idx] = nums[idx], nums[pointer]
                pointer += 1 
        return pointer
            
            