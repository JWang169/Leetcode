class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if not arr:
            return -1
        count = collections.Counter(arr)
        nums = list(count.keys())
        nums.sort(reverse=True)
        for num in nums:
            if num == count[num]:
                return num
        return -1 
        
        