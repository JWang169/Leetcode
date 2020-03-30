class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        records = dict()
        for student, score in items:
            scores = records.get(student, [])
            heapq.heappush(scores, score)
            if len(scores) > 5:
                heapq.heappop(scores)
            
            records[student] = scores
        
        result = []
        for student, scores in records.items():
            result.append([student, sum(scores) // 5])
        
        return result
        
        