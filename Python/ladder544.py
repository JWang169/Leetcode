import heapq 
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        if not nums:
            return []
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        
        results = []
        for _ in range(k):
            num = heapq.heappop(heap)
            results.append(-num)
        return results