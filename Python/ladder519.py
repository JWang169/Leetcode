class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        intervals = [[0, 359, 1]]
        i = 1
        while i < n:
            i += 1
            ma = 0
            idx = -1
            
            for m, interval in enumerate(intervals):
                if interval[1] - interval[0] > ma:
                    idx = m
                    ma = interval[1] - interval[0]
                    
            x, y, z = intervals[idx]

            n1 = [x, (x + y) // 2, z]
            n2 = [(x + y) // 2 + 1, y, i]
            intervals[idx] = n1
            intervals.append(n2)
        
        intervals.sort()
        return intervals
            
            
        
    