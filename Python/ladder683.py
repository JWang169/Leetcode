class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        if not s or not dict:
            return 0
        s = s.lower()
        words = set([word.lower() for word in dict])
        n = len(s)
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(i, n):
                if s[i: j + 1] in words:
                    dp[i][j] = 1 
        
        for i in range(n):
            for j in range(i, n):
                for k in range(i, j):
                    dp[i][j] += dp[i][k] * dp[k + 1][j]
        
        return dp[0][-1]