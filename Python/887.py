# april 8  依然不会做
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # 1. 这个骚操作我自己肯定是想不出来
        # 噢我懂了，就是dp[i][j]代表我现在有j个鸡蛋，然后我站在i楼，问最多能测到多少层楼。应该是这么一说。
        # dp = [[0] * (K + 1) for _ in range(N + 1)]
        # for i in range(1, N + 1):
        #     for j in range(1, K + 1):
        #         dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + 1
        #     if dp[i][j] >= N:
        #         return i
        
        
        
        # 2. 笨方法dp
        
        # dp[i][j]: how many steps do we need to test j floors with i eggs
        # 如果在j层蛋碎了，现在你的范围就缩小到j-1层了，因为i以上就一定超过了F， 不用再考虑。而且碎了一个蛋，还剩i-1个蛋： dp[i][j] => dp[i - 1][j - 1]
        # 如果在第j层蛋没碎，下一步就在剩下的 N - i层里搜索，蛋的个数不变=>dp[i][n - j]
        dp = [[sys.maxsize] * (N + 1) for _ in range(K + 1)]

        for j in range(1, N + 1):
            dp[0][j] = 0
            dp[1][j] = j 
        
        for i in range(K + 1):
            dp[i][0] = 0
        
        for i in range(2, K + 1):
            for j in range(1, N + 1):
                # binary search
                left, right = 1, j
                while left <= right:
                    mid = (left + right) // 2
                    if dp[i - 1][mid - 1] > dp[i][j - mid]:
                        right = mid - 1
                    else:
                        left = mid + 1
                    dp[i][j] = min(dp[i][j], max(dp[i - 1][mid - 1], dp[i][j - mid]) + 1)
                
        return dp[-1][-1]
    
    
        

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
        