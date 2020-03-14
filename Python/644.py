class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left, right = min(nums), max(nums)

        while left + 10e-6 < right:
            mid = (left + right) / 2 
            presum = [0]
            for num in nums:
                presum.append(presum[-1] + num - mid)   

            minPre = 0 # start from the beginning 
            found = False
            for i in range(k, len(nums) + 1):
                if presum[i] - minPre >= 0:
                    found = True
                    break
                minPre = min(minPre, presum[i - k + 1])
            
            if found:
                left = mid
            else:
                right = mid 
                
        return left
            
            
            