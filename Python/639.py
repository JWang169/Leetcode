class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        mod = 1000000007
        n = len(s)
        f = [0] * (n + 1)
        f[0] = 1
        for i in range(1, n + 1):
            if s[i - 1] == '*':
                f[i] = (f[i] + 9 * f[i - 1]) % mod
                if i >= 2:
                    t = 0
                    if s[i - 2] == '*':
                        f[i] = (f[i] + 15 * f[i - 2]) % mod
                    elif s[i - 2] == '1':
                        f[i] = (f[i] + 9 * f[i - 2]) % mod
                    elif s[i - 2] == '2':
                        f[i] = (f[i] + 6 * f[i - 2]) % mod
            else:
                if s[i - 1] >= '1' and s[i - 1] <= '9':
                    f[i] = (f[i] + f[i - 1]) % mod
                if i >= 2:
                    if s[i - 2] == '*':
                        t = 0
                        if s[i - 1] >= '0' and s[i - 1] <= '6':
                            f[i] = (f[i] + 2 * f[i - 2]) % mod
                        elif s[i - 1] >= '7' and s[i - 1] <= '9':
                            f[i] = (f[i] + f[i - 2]) % mod
                    else:
                        twoDigits = int(s[i - 2 : i])
                        if twoDigits >= 10 and twoDigits <= 26:
                            f[i] = (f[i] + f[i - 2]) % mod
        return f[n]