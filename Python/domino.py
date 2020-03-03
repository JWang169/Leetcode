class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # check there are enough same values
        if len(A) != len(B):
            return -1
        countA = [0] * 7
        countB = [0] * 7
        same = [0] * 7
        for i in range(len(A)):
            a, b = A[i], B[i]
            countA[a] += 1 
            countB[b] += 1
            if a == b:
                same[a] += 1
        
        for i in range(1, 7):
            if countA[i] + countB[i] - same[i] == len(A):
                return len(A) - max(countA[i], countB[i])
        return -1