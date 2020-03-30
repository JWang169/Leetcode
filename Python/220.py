class Solution:
    # bucket sort
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k < 0 or t < 0:
            return False 
        
        buckets = {}
        
        for i, num in enumerate(nums):
            # There are t nums in a bucket
            bucketId = num // t if t != 0 else num
            cans = [bucketId - 1, bucketId, bucketId + 1]
            for idx in cans:
                if idx in buckets and abs(buckets[idx] - num) <= t:
                    return True
            
            buckets[bucketId] = num
            
            if i >= k:
                expired = nums[i - k] // t if t != 0 else nums[i - k]
                del buckets[expired]
        return False 




# bruteforce TLE
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i in range(len(nums) - 1):
            left = i + 1
            right = min(len(nums), i + k + 1)
            sub = list(nums[left: right])
            sub.sort()
            idx = bisect.bisect_left(sub, nums[i])
            if idx > 0 and nums[i] - sub[idx - 1] <= t:
                return True
            elif idx < len(sub) and sub[idx] - nums[i] <= t:
                return True
            
        return False 
        
        
        
        
        