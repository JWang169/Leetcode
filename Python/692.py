class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        counter = collections.Counter(words)
        for word, num in counter.items():
            heapq.heappush(heap, (-num, word))
        
        result = []
        for i in range(k):
            if heap:
                num, word = heapq.heappop(heap)
                result.append(word)
            else:
                break
        return result