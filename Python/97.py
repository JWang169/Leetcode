class Solution:
        # s3的最后一个字符是从s1尾巴来的或者s2尾巴来的
        # s3的前i个字符是s1的前个字符和s2的前k个字符交错形成的
        # 降维， i = j + k， 不用开三维数组， 降到2维
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        f = [[False] * (n + 1) for _ in range(m + 1)]
        
        
        f[0][0] = True
        for i in range(0, m + 1):
            for j in range(0, n + 1):
                if i == 0 and j == 0:
                    continue
                if j == 0:
                    f[i][j] = f[i - 1][j] and s1[i - 1] == s3[i - 1]
                    continue
                if i == 0:
                    f[i][j] = f[i][j - 1] and s2[j - 1] == s3[j - 1]
                    continue
            
                if (s2[j - 1] == s3[i + j - 1] and f[i][j - 1]) or (s1[i - 1] == s3[i + j - 1] and f[i - 1][j]):
                    f[i][j] = True
        return f[-1][-1]
    
        
        