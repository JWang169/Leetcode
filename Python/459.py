class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # right = 0
        # while right < len(s) - 1:
        #     pattern = s[:right + 1]
        #     matched = s.split(pattern)
        #     if not any(matched):
        #         return True
        #     else:
        #         right += 1
        # return False 
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
 