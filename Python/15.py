class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 1):
            if i > 0 and nums[i - 1] == nums[i]:
                continue 
            target = 0 - nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[left] + nums[right]
                if curSum == target:
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1 
                    left += 1 
                    right -= 1 
                elif curSum > target:
                    right -= 1 
                else:
                    left += 1 
        return results