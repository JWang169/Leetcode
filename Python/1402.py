class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        if not satisfaction:
            return 0
        satisfaction.sort()
        if satisfaction[-1] < 0:
            return 0
        n = len(satisfaction)
        ma = 0
        # start 
        for i in range(n - 1, -1, -1):
            # end
            count = 0
            idx = 1
            for j in range(i, n):
                count += idx * satisfaction[j]
                idx += 1 
            ma = max(ma, count)
        return ma 
            