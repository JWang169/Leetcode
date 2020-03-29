class Solution:
    def numTeams(self, rating: List[int]) -> int:
        result = 0
        for i in range(len(rating) - 2):
            for j in range(i + 1, len(rating) - 1):
                remains = list(rating[j + 1: ])
                remains.sort()
                idx = bisect.bisect_left(remains, rating[j] + 1)
                if rating[i] < rating[j]:
                    result += len(remains) - idx 
                elif rating[i] > rating[j]:
                    result += idx 
        return result 
        