class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        nums1 = [n.lstrip('0') for n in nums1]
        nums2 = [n.lstrip('0') for n in nums2]
        
        for i, n1 in enumerate(nums1):
            if n1 == '':
                n1 = '0'
            if i >= len(nums2) or nums2[i] == '':
                n2 = '0'
            else:
                n2 = nums2[i]
            
            if int(n1) > int(n2):
                return 1
            elif int(n2) > int(n1):
                return -1
        
        if len(nums1) < len(nums2):
            for i in range(len(nums1), len(nums2)):
                if nums2[i] != '':
                    return -1
        return 0
            