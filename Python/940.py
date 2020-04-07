class Solution(object):
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        # abb
        # a, /b, ab, /abb
        
        MOD = 10 ** 9 + 7
        counter = [0] * 26
        for ch in S:
            idx = ord(ch) - ord('a')
            counter[idx] = sum(counter) + 1
        return sum(counter) % MOD