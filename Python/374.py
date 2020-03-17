# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n
        while left + 1 < right:
            mid = (left + right) // 2 
            res = guess(mid)
            if res == 0:
                print('found')
                return mid 
            if res == 1:
                left = mid + 1
            else:
                right = mid - 1
        if guess(left) == 0:
            return left 
        return right 