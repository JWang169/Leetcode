"""
dp类型的题

dp[i][j]代表把word1[:i]变成word2[:j]需要多少步
initial status: dp[0][j] = j
meaning we need j steps to make word1[:0] (which is "") to word2[:j]. We can only add letters to make a "" to a string
so is dp[i][0]

then we iterate all letters in word1, starting from the first letter in word1
we make word1[ :1] into word2[ :j]
1. if word1[i - 1] == word2[j - 1], meaning the current letter is the same, we dont need any change
so we have dp[i][j] = dp[i - 1][j - 1], the current status depends on the previous status.
(one redundent explaination, we have made word1[:i - 1] equal to word[:j - 1] by making dp[i - 1][j - 1] steps,
so now, all we need next is based on the dp[i-1][j-1], no need to consider the steps previous than this.)
2. if word1[i - 1] != word2[j - 1], meaning the current letter is different. 
we will make word1[:i] and word2[:j] from the previous step. 
there are three previous status we can use to achieve this step:
1. we make word1[:i] to word2[:j-1], and add word2[j - 1] to word1[:i] => dp[i][j - 1] + 1
2. we make word1[:i - 1] to word2[:j-1], and replace word1[i - 1] with word2[j - 1] => dp[i - 1][j - 1] + 1 
3. we make word1[:i] to word1[: i -1], which equals to word2[:j] => dp[i - 1][j] + 1

"""



class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 先看最后一个， horse的e是怎么变成ros的s的
        # 有增加，删除，替换三种方法
        # 增加就是a[i] 变成 b[j-1], 然后再在a.append(b[j])
        # 替换就是a[i] 换成 b[j]
        # 删除就是删除a[i]， a[i - 1] == b[j] 
        # 还有第四种情况，就是a[i] == b[j]， 什么都不用动
        # f[i][j] = min{f[i][j - 1] + 1 => 插入, f[i - 1]f[j - 1] + 1替换, f[i - 1][j] + 1 => 删除, f[i - 1][j - 1] | a[i] == b[j]}
        # 初始条件：f[0][j] = j, j = 0, ...n
        #         f[i][0] = i, i = 0, ... m
        # 计算顺序：f[0][0...n]...
        #         f[m][0...n]
         
        m, n = len(word1), len(word2)
        f = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1): 
            f[i][0] = i
        for j in range(n + 1):
            f[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = min(f[i - 1][j - 1], f[i][j - 1], f[i - 1][j]) + 1
        return f[m][n]