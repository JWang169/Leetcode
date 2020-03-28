class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        
        swap = 0
        a, b = None, None
        for i in range(len(A)):
            if A[i] != B[i]:
                if swap == 0:
                    a, b = A[i], B[i]
                    swap = 1
                elif swap == 2:
                    return False
                else:
                    if a == B[i] and b == A[i]:
                        swap = 2
                    else:
                        return False 
        if swap == 2:
            return True
        if swap == 0 and len(set(A)) < len(A):
            return True
        return False 
                    