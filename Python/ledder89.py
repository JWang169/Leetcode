class Solution:
    """
    @param A: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def kSum(self, A, k, target):
        # 最后一步：最后一个数是否选入k个数之中
        # f[i][k][s]: 表示有多少种方法可以在前i个数种选出k个，使他们的和是s
        # 转移方程: f[i][k][s] = f[i - 1][k][s] + f[i - 1][k - 1][s - A(i - 1)] | k >= 1 and s >= A(i - 1)
        # f[i - 1][k][s]: A(i-1)不选
        # f[i - 1][k - 1][s - A(i - 1)] | k >= 1 and s >= A(i - 1)：A(i - 1)选，前面的选k-1个
        
        
        
        f = [[[0] * (target + 1) for i in range(k + 1)] for j in range(len(A) + 1)]
        # 前0个数选0个， 和是s（不可能发生的就是0）
        for i in range(target + 1):
            f[0][0][i] = 0
            
        f[0][0][0] = 1 
        
        for i in range(1, len(A) + 1):
            for j in range(k + 1):
                for n in range(target + 1):
                    f[i][j][n] = f[i - 1][j][n]
                    if j >= 1 and n >= A[i - 1]:
                        f[i][j][n] += f[i - 1][j - 1][n - A[i - 1]]
        
        
        return f[len(A)][k][target]