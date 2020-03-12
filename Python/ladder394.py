class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        dp = [True] * 3
        dp[0] = False
        # dp[1] = True 
        # dp[2] = True 
        for i in range(3, n + 1):
            if dp[i - 1] == False or dp[i - 2] == False:
                dp.append(True) 
            else:
                dp.append(False) 
        return dp[n]
        
        