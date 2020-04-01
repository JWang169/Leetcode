class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        for i in range(1, N + 1):
            for j in range(1, K + 1):
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
            if dp[i][j] >= N:
                return i
        
        
        
        """

        # dp[i][j]: moves with i eggs and j floor
        dp = [[sys.maxsize] * (N + 1) for _ in range(K + 1)]
        # 0 floor: no move needed
        # k eggs 1 floor. only one move needed
        for i in range(K + 1):
            dp[i][1] = 1
            dp[i][0] = 0
        # n floor 1 egg. need n moves, from 1 floor to n floor
        for i in range(1, N + 1):
            dp[1][i] = i  
        
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                # we have i eggs, and j floors.
                # now we want to find floor k, where we should drop eggs on.
                 for k in range(1, j + 1):
                    # 1. If the egg breaks on kth floor, then we goes to dp[i - 1][k - 1]
                    # because we lost an egg and k is not the N we're looking for.
                    # 2. if the egg doesn't break at kth floor, then we still have the egg.
                    # we know n is larger than k, we exclude the floors smaller than k and move to dp[i][j - k] 
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]
        """
        