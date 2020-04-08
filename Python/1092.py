class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        sub = self.lcs(str1, str2)
        cur = ""
        p1, p2 = 0, 0
        for ch in sub:
            while p1 < len(str1) and str1[p1] != ch:
                cur += str1[p1]
                p1 += 1
            while p2 < len(str2) and str2[p2] != ch:
                cur += str2[p2]
                p2 += 1 
            cur += ch
            p1 += 1 
            p2 += 1 
        return cur + str1[p1:] + str2[p2:]
    
    
    def lcs(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[""] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], key=len)    
        return dp[-1][-1]
