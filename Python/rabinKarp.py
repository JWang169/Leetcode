class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        if target is None or source is None:
            return -1 
            
        if len(target) == 0:
            return 0 
            
        if len(source) == 0:
            return -1
            
        MOD = 10e7
        m = len(target)
        if m == 0:     
            return 0
        
        power = 1 
        for i in range(m):
            power = power * 31 % MOD 
        
        targetCode = 0 
        for t in target:
            targetCode = (targetCode * 31 + ord(t)) % MOD 
        
        hashCode = 0 
        for i in range(len(source)):
            hashCode = (hashCode * 31 + ord(source[i])) % MOD 
            if i < m - 1:
                continue 
            
            if i >= m:
                hashCode = hashCode - (ord(source[i - m]) * power) % MOD 
                if hashCode < 0:
                    hashCode += MOD
            
            if hashCode == targetCode and source[i - m + 1: i + 1] == target:
                return i - m + 1 
        return -1 
        
        
        
        
        
        