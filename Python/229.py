class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0, 0
        can1, can2 = None, None
        for n in nums:
            if can1 == n:
                count1 += 1 
            elif can2 == n:
                count2 += 1 
            elif count1 == 0:
                count1 += 1 
                can1 = n
            elif count2 == 0:
                count2 += 1 
                can2 = n
            else:
                count1 -= 1
                count2 -= 1
        
        res = []
        if nums.count(can1) > len(nums) / 3:
            res.append(can1)
        if nums.count(can2) > len(nums) / 3:
            res.append(can2)
        return res
            