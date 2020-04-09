class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if n % k or n // k <= 0:
            return False 
        
        counter = collections.Counter(nums)
        keys = sorted(list(counter.keys()))
        start = 0
        m = n // k
        
        while m > 0:
            while keys[start] not in counter:
                start += 1 
            idx = keys[start]
            for i in range(k):
                if idx not in counter:
                    return False 
                counter[idx] -= 1 
                if counter[idx] == 0:
                    del counter[idx]
                idx += 1 
            m -= 1
        return True 
                    
                
            
            
        
        