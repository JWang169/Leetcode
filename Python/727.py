# Mar 31  总结
class Solution:
    def minWindow(self, S: str, T: str) -> str:
        m, n = len(S), len(T)
        dp = [[sys.maxsize] * (n + 1)  for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
            # the letters in T are in sequence. 
            # we must find T[:1] first
                if T[j - 1] == S[i - 1]:
                    # this is the first letter in T we find. we set dp[i][j] to 1
                    if j == 1:
                        dp[i][j] = 1
                        
                    # if this is not T[0], it will depends on the previous status. If we didn't find T[:j - 1] in the previous sequence, then dp[i - 1][j - 1] will be sys.maxsize, dp[i][j] will also be sys.maxsize. 
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                # 如果没找到新的相等的letter，就延续上一个status, 但S又遍多了一位，即使和T没有match，但长度也要+1
                else:
                    dp[i][j] = dp[i - 1][j] + 1
        
        # print(dp)
        start, end = 0, m + 1
        length = sys.maxsize
        for i in range(m + 1):
            if dp[i][n] < length:
                length = dp[i][n]
                end = i
                start = i - length
        if length < sys.maxsize:
            return S[start: end]
        return ""
        


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
                
        
        
        