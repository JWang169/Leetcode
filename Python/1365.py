class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        s = sorted(nums)
        result = []
        for num in nums:
            idx = bisect.bisect_left(s, num)
            result.append(idx)
        return result
        
        
        