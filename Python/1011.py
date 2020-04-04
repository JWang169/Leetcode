class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        if not weights:
            return 1
        
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = (left + right) // 2
            day = self.days(mid, weights)
            if day > D:
                left = mid
            else:
                right = mid 
        
        day = self.days(left, weights)
        if day <= D:
            return left
        return right
        
    
    def days(self, cap, weights):
        count = 1
        cumsum = 0
        for weight in weights:
            cumsum += weight
            if cumsum > cap:
                count += 1 
                cumsum = weight
            
        return count 
        
        