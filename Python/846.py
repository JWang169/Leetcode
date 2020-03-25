class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False 
        
        nums = collections.Counter(hand)
        heap = list(nums.keys())
        heapq.heapify(heap)
        
        for i in range(len(hand)):
            if i % W == 0:
                while heap[0] not in nums:
                    heapq.heappop(heap)
                start = heap[0]
                prev = start 
                nums[start] -= 1 
                if nums[start] == 0:
                    del nums[start]
                continue
                    
            if prev + 1 not in nums:
                return False
            
            nums[prev + 1] -= 1 
            if nums[prev + 1] == 0:
                del nums[prev + 1]
            prev += 1 
        
        return True 
    
    
                    