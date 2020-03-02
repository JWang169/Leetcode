public class DecodeWaysII {
    private int cnt1(char c) {
        if (c == '0') {
            return 0;
        }
        
        if (c != '*') {
            return 1;
        }
        
        return 9;
    }
    
    private int cnt2(char c2, char c1) {
        if (c2 == '0') {
            return 0;
        }
        
        if (c2 == '1') {
            if (c1 == '*') {
                return 9;
            }
            
            return 1;
        }
        
        if (c2 == '2') {
            if (c1 == '*') {
                return 6;
            }
            
            if (c1 <= '6') {
                return 1;
            }
            
            return 0;
        }
        
        if (c2 >= '3' && c2 <= '9') {
            return 0;
        }
        
        // c2 == '*'
        if (c1 >= '0' && c1 <= '6') {
            return 2;
        }
        
        if (c1 >= '7' && c1 <= '9') {
            return 1;
        }
        
        return 15;
    }
    
    public int numDecodings(String ss) {
        char[] s = ss.toCharArray();
        int n = s.length;
        long MOD = 1000000007;
        
        long[] f = new long[n + 1];
        f[0] = 1;
        for (int i = 1; i <= n; ++i) {
            // last digit to letter
            f[i] = f[i - 1] * cnt1(s[i - 1]);
            if (i > 1) {
                f[i] += f[i - 2] * cnt2(s[i - 2], s[i - 1]);
            }
            
            f[i] %= MOD;
        }
        
        return (int)f[n];
    }
}