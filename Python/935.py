class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10
        
        prev = [1] * 10
        paths = {0: [4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[3, 9, 0], 5: [], 
                 6: [1, 7, 0], 7:[2, 6], 8:[1, 3], 9:[2, 4]}
        for i in range(1, N):
            cur = [0] * 10
            for j in range(10):
                for num in paths[j]:
                    cur[j] += prev[num]
            prev = cur
        MOD = 10 ** 9 + 7
        return sum(prev) % MOD
    
            
        
        
        