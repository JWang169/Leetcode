class Solution:
    """
    @param A: An integer array
    @param start: An integer
    @param end: An integer
    @return: the number of possible answer
    """
    def subarraySumII(self, A, start, end):
        preSum = 0
        s = [0]  # list of preSum, len(s) = len(A) + 1
        for num in A:
            preSum += num
            s.append(preSum)
        
        count = 0
        rStart, rEnd = 0, 0
        # 对每个左端点j，找到rStart 和 rEnd， 在这个区间内， rEnd - rStart + 1 就是以j为左端点符合条件的字数组的数量
        for j in range(len(s)): 
            while rStart < len(s) and s[rStart] - s[j] < start:
                rStart += 1 
            while rEnd < len(s) and s[rEnd] - s[j] <= end:
                rEnd += 1 
            if (rStart > j):
                count += rEnd - rStart 
        return count 
                