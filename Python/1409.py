class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        当成01背包问题做，但我可能还是没懂
        dp代表小的那堆，就是从stones里面能不能拿出几个stone组成sum为i。如果能dp[i] = True
        从头开始遍历for stone in stones, 用cumsum记录当前的总和 cumsum += stone，
        然后把能取到的i都置为1, 就相当于遍历原有的dp，在原有的基础上+stone。就是新增的可以取到的dp: if dp[i - stone]: dp[i] = 1
        更新dp之后，再遍历一次，找最接近total / 2 的地方。找到了就return
        '''

        dp = [0] * 3000
        dp[0] = 1
        cumsum = 0
        for stone in stones:
            cumsum += stone 
            dp[cumsum] = 1
            for i in range(cumsum, stone - 1, -1):
                if dp[i - stone]:
                    dp[i] = 1
        
        for i in range(cumsum // 2, -1, -1):
            if dp[i]:
                return cumsum - 2 * i
        return 0        
        