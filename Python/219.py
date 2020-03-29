class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                return True 
            else:
                seen.add(num)
            if i < k:
                continue 
            last = nums[i - k]
            seen.remove(last)
        
        return False 