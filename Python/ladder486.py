import heapq
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # write your code here
        heap = []
        for i in range(len(arrays)):
            if len(arrays[i]) > 0:
                heapq.heappush(heap, [arrays[i][0], i, 0])
                
        result = []
        while heap:
            num, arr, idx = heapq.heappop(heap)
            result.append(num)
            if idx + 1 < len(arrays[arr]):
                heapq.heappush(heap, [arrays[arr][idx + 1], arr, idx + 1])
        
        return result
