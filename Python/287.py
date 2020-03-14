class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return -1
        left, right = 1, len(nums)
        while left + 1 < right:
            mid = (left + right) // 2 
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1 
            if count > mid:
                right = mid
            else:
                left = mid 

        count = 0
        for num in nums:
            if num <= left:
                count += 1 
        if count > left:
            return left
        else:
            return right