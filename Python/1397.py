class Solution:
    def findGoodStrings(self, n, s1, s2, evil):
        M = 10 ** 9 + 7
        m = len(evil)
        memo = {}
        
        # KMP
        dfa = self.failure(evil)

        def dfs(i, x, bound):
            if x == m:
                return 0
            if i == n:
                return 1
            if (i, x, bound) not in memo:
                cnt = 0
                lo = ord('a' if bound & 1 else s1[i])  # "be*" -> {"be*", "ca*", ..}, 'b' when bound bit = ?0
                hi = ord('z' if bound & 2 else s2[i])  # "do*" -> {"cz*", "do*", ..}, 'd' when bound bit = 0?
                for j, c in enumerate(chr(o) for o in range(lo, hi + 1)):
                    y = x
                    while y and evil[y] != c:
                        y = dfa[y - 1]
                    y += evil[y] == c
                    cnt = (cnt + dfs(i + 1, y, bound | (j > 0) | (j < hi - lo) << 1)) % M
                memo[i, x, bound] = cnt
            return memo[i, x, bound]
			
        return dfs(0, 0, 0)

    def failure(self, evil):
        res = [0] * len(evil)
        i, j = 1, 0
        while i < len(evil):
            if evil[i] == evil[j]:
                res[i] = j + 1
                j += 1 
                i += 1 
            elif j != 0:
                j = res[j - 1]
            else:
                res[i] = 0
                i += 1 
        return res 
        
        
        
        
        
        