class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        A1 = set()
        B1 = set()

        for i in range(n):
            for j in range(n):
                if B[i][j] == 1:
                    B1.add((i, j))
                if A[i][j] == 1:
                    A1.add((i, j))
        
        
        dx = [i for i in range(1, n)] + [0] + [-i for i in range(1, n)]
        dy = dx 
        result = 0
        
        for i in range(len(dx)): 
            for j in range(len(dy)):
                count = 0
                for ax, ay in A1:
                    if (ax + dx[i], ay + dy[j]) in B1:
                        count += 1 
                result = max(result, count)
            
        return result 
        
        
        
        