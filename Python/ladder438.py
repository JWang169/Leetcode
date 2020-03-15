class Solution:
    """
    @param n: An integer
    @param times: an array of integers
    @return: an integer
    """
    def copyBooksII(self, n, times):
        if n == 0:
            return 0
        
        left, right = min(times), min(times) * n 
        while left + 1 < right:
            mid = (left + right) // 2 
            total = 0
            for time in times:
                total += mid // time 
            
            if total >= n:
                right = mid
            else:
                left = mid 
        
      
        total = 0
        for time in times:
            total += left // time 
        
        
        if total >= n:
            return left
        return right
        