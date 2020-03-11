import heapq
class Solution:
    """
    @param nums: A list of integers
    @return: the median of numbers
    """
    def medianII(self, nums):
        minHeap = []
        maxHeap = []
        results = []
        for i in range(len(nums)):
            #push
            if len(minHeap) < len(maxHeap):
                heapq.heappush(minHeap, nums[i])
            else:
                heapq.heappush(maxHeap, -nums[i])
            
            # swap if needed 
            # -maxHeap[0] is the max number of the smaller half
            if maxHeap and minHeap and -maxHeap[0] > minHeap[0]:
                mi = heapq.heappop(minHeap)
                ma = -heapq.heappop(maxHeap)
                heapq.heappush(minHeap, ma)
                heapq.heappush(maxHeap, -mi)
                
            # pop 
            if len(maxHeap) >= len(minHeap):
                results.append(-maxHeap[0])
            else:
                results.append(minHeap[0])
        
        return results