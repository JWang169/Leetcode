class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1 
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return[left + 1, right + 1]
            if curSum > target:
                right -= 1 
            else:
                left += 1 
        return []
            