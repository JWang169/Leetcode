class Solution:
    def minWindow(self, S: str, T: str) -> str:
        # KMP  => if this is ask for substring, KMP will be the answer 
        # DP => yep
        if not T:
            return ""
        if not S:
            return None 
        
        m, n = len(S), len(T)
        dp = [[sys.maxsize] * (n + 1) for _ in range(m + 1)]
        # dp[i][j]: minimum substring length at S[i] which contains subsequence of T[:j]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if S[i - 1] == T[j - 1]:
                    if j == 1:
                        dp[i][j] = 1 
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = dp[i - 1][j] + 1
           
        # print(dp)
        start, end = 0, m + 1
        length = sys.maxsize
        for i in range(1, m + 1):
            if dp[i][n] < length:
                length = dp[i][n] 
                end = i
                start = end - length
        if length < sys.maxsize:
            return S[start: end]
        return ""
                
        
        
        