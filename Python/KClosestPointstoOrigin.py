import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        if K == 0:
            return []
        heap = []

        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, [-dist, point])
            if len(heap) > K:
                heapq.heappop(heap)
        results = []
        for i in range(len(heap)):
            results.append(heapq.heappop(heap)[1])
        return results
        # return list(map(lambda x: x[1], h))