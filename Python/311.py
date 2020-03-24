class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = [[0] * len(B[0]) for _ in range(len(A))]
        # result[i][j] = A[i][:] * B[:][j]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] != 0:
                    for k in range(len(B[0])):
                        result[i][k] += A[i][j] * B[j][k]
        return result
        
        
        