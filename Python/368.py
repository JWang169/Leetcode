class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        
        f = [1] * len(nums)
        prev = [-1] * len(nums)
        ma = 0
        index = 1
        
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if 1 + f[j] > f[i]:
                        f[i] = 1 + f[j]
                        prev[i] = j
            if f[i] > ma:
                ma = f[i]
                index = i
            
        
        result = []
        for i in range(ma):
            result.append(nums[index])
            index = prev[index]
        return result
        