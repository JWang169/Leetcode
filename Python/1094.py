from heapq import heappop, heappush 
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        for num, start, end in trips:
            heappush(heap, (end, 0, num))
            heappush(heap, (start, 1, num))
        
        total = 0
        while heap:
            cur, act, num = heappop(heap)
            if act == 0:
                total -= num
            else:
                total += num
            if total > capacity:
                print(heap)
                return False
            
        return True 