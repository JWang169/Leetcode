class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """
    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        
        left, right = 0, max(L)
        while left + 1 < right:
            mid = (left + right) // 2
            count = 0
            for l in L:
                count += l // mid 
            if count >= k:
                left = mid 
            else:
                right = mid 
                
        print(left, right)
        count = 0
        for l in L:
            count += l // right
        
        return right if count >= k else left