class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # quick select 
        # find the nth in two arrays
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n // 2 )
        else:
            first = self.findKth(nums1, nums2, n // 2 - 1 )
            second = self.findKth(nums1, nums2, n // 2)
            return (first + second) / 2
    
    
    def findKth(self, nums1, nums2, k):
        if len(nums1) == 0:
            return nums2[k]
        if len(nums2) == 0:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
            
        idx1, idx2 = len(nums1) // 2, len(nums2) // 2
        mid1 = nums1[idx1]
        mid2 = nums2[idx2]
        
        if idx1 + idx2 < k:
            if mid1 < mid2:
                return self.findKth(nums1[idx1 + 1: ], nums2, k - idx1 - 1)
            else:
                return self.findKth(nums2[idx2 + 1: ], nums1, k - idx2 - 1)
        # k is smaller than the sum of idx1 and idx2, meaning the second half wont be included
        else:
            if mid1 > mid2:
                return self.findKth(nums1[:idx1], nums2, k)
            else:
                return self.findKth(nums1, nums2[:idx2], k)