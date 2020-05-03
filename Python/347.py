class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        heap = []
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))
        
        result = []
        for i in range(k):
            freq, num = heapq.heappop(heap)
            result.append(num)
            
        return result
            
            