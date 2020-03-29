class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix or not matrix[0]:
            return None 
        m, n = len(matrix), len(matrix[0])
        result = -sys.maxsize
        
        for r1 in range(m):
            for r2 in range(r1 + 1, m + 1):
                nums = self.getNums(r1, r2, matrix)   
                # pres[i]: sum(nums[: i])
                pres = [0] * (n + 1)
                for i in range(n):
                    pres[i + 1] = pres[i] + nums[i] 
                    if pres[i + 1] == k:
                        return k

                for i in range(1, n + 1):
                    # result = pres[i] - pres[j]
                    # we want target >= pres[i] - k      
                    closest = self.search(list(pres), i, k)
                    if abs(k - (pres[i] - closest)) < abs(k - result):
                        result = pres[i] - closest

        return result
    
        
    def search(self, pres, i, k):
        sum1 = pres[i]
        cans = sorted(pres[:i])
        target = sum1 - k 
        idx = bisect.bisect_left(cans, target)
        return cans[idx] if idx < len(cans) else cans[-1]

    
    def getNums(self, r1, r2, matrix):
        nums = [0] * len(matrix[0])
        for j in range(len(nums)):
            for i in range(r1, r2):
                nums[j] += matrix[i][j]
    
        return nums
        
        

        
        