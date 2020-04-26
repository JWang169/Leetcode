class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        right1, right2 = m - 1, n - 1

        end = m + n - 1 

        while end >= 0 and right2 >= 0 and right1 >= 0:
            if nums1[right1] > nums2[right2]:
                nums1[end] = nums1[right1]
                right1 -= 1 
            else:
                nums1[end] = nums2[right2]
                right2 -= 1
            end -= 1 
        
        while end >= 0 and right2 >= 0:
            nums1[end] = nums2[right2]
            end -= 1 
            right2 -= 1 
        
        