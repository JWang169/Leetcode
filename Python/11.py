"""
June 18, 2020

Two pointer, surprise surprise 

"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            width = right - left
            res = max(res, width * min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1 
            else:
                right -= 1 
        return res 