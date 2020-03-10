class Solution:
    def trap(self, height: List[int]) -> int:
        # min(左边第一比它大和右边第一比它大的) - 自己的高度
        if not height:
            return 0
        left = [0] * len(height)
        right = [-1] * len(height)
        for i in range(1, len(height)):
            if height[left[i - 1]] > height[i]:
                left[i] = left[i - 1]
            else:
                left[i] = i
            
        for i in range(-2, -len(height) - 1, -1):
            if height[right[i + 1]] > height[i]:
                right[i] = right[i + 1]
            else:
                right[i] = i
        
        result = 0
        for i in range(len(height)):
            cur = min(height[left[i]], height[right[i]])
            result = result + cur - height[i]
        return result        