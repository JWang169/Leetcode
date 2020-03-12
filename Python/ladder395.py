class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """

    def firstWillWin(self, values):
        if not values:
            return False
        n = len(values)
        f = [0] * (n + 1)
        f[n - 1] = values[n - 1]
        for i in range(n - 2, -1, -1):
            f[i] = max(values[i] - f[i + 1], values[i] + values[i + 1] - f[i + 2])
        return f[0] > 0


# f[i]为一方在面对a[i...n - 1]这些数字时， 能得到的最大的与对手的数字差
# 转移房产：f[i] = max{a[i] - f[i + 1], a[i] + a[i + 1] - f[i + 2]}