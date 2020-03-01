public class LongestPalindromicSubstring {
    /**
     * @param s: input string
     * @return: the longest palindromic substring
     */
    public String longestPalindrome(String s) {
        // write your code here
        int n = s.length();
        int longest = 1, start = 0, end = 1;
        
        boolean[][] dp = new boolean[n][n];
        for(int i = 0; i < n; i++){
            dp[i][i] = true;
        }
        for(int i = 1; i < n; i++){
            if(s.charAt(i - 1) == s.charAt(i)) {
                dp[i - 1][i] = true; 
                longest = 2;
                start = i - 1;
                end = i + 1;
            }
            // else dp[i - 1][i] = false;
        }
        
        for(int len = 2; len < n; len++){
            for(int left = 0; left < n - len; left++){
                int right = left + len;
                dp[left][right] = dp[left + 1][right - 1] && (s.charAt(left) == s.charAt(right));
                
                if(dp[left][right] && (len + 1 > longest)){
                    longest = len + 1;
                    start = left;
                    end = right + 1;
                    // System.out.println(start);
                    // System.out.println(end);
                    // System.out.println(longest);
                    
                }
            }
        }
        
        return s.substring(start, end);
    }
}