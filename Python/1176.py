class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        if not calories:
            return 0
        n = len(calories)
        prefix = [0] * (n + 1)
        
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + calories[i - 1]
        
        point = 0
        for i in range(n + 1 - k):
            cal = prefix[i + k] - prefix[i]
            if cal < lower:
                point -= 1
            if cal > upper:
                point += 1 
        return point
        
        
        