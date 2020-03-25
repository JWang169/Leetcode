class Solution:
    def numberOfSteps (self, num: int) -> int:
        if num == 0:
            return 0
        count = 0
        while num > 0:
            count += (num & 1) + 1
            num >>= 1
        return count - 1