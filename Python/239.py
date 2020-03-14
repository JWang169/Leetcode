from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        # if len(nums) == k:
        #     return [max(nums)]

        queue = deque()
        # queue.append(0)
        results = []
        for idx in range(len(nums)):
            num = nums[idx]
            if queue and queue[0] <= idx - k:
                queue.popleft()
            
            while len(queue) > 0 and nums[queue[-1]] < num:
                queue.pop()
            queue.append(idx)
            
            if idx >= k - 1:
                results.append(nums[queue[0]])  
                
        return results
        
