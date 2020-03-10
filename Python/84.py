class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        heights.append(-1)
        for i, h in enumerate(heights):
            while len(stack) > 0 and heights[stack[-1]] >= h:
                lastHeight = heights[stack.pop()]
                left = stack[-1] + 1 if len(stack) > 0 else 0
                right = i - 1
                curArea = lastHeight * (right - left + 1)
                maxArea = max(maxArea, curArea)
            stack.append(i)
        
        return maxArea