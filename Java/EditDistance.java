public class EditDistance {
    /**
     * @param word1: A string
     * @param word2: A string
     * @return: The minimum number of steps.
     */
    public int minDistance(String word1, String word2) {
        // write your code here
        int m = word1.length();
        int n = word2.length();
        // dp[i][j]表示把长度为i的word1转换成长度为j的word2需要的步数
        int[][] dp = new int[m + 1][n + 1];
        for(int i = 0; i < m + 1; i++){
            dp[i][0] = i;
        }
        for(int j = 0; j < n + 1; j++){
            dp[0][j] = j;
        }
        for(int i = 1; i < m + 1; i++){
            for(int j = 1; j < n + 1; j++){
                if(word1.charAt(i - 1) == word2.charAt(j - 1)){
                    dp[i][j] = dp[i - 1][j - 1];
                }
                else{
                    dp[i][j] = Math.min(dp[i - 1][j - 1], Math.min(dp[i - 1][j], dp[i][j - 1])) + 1;
                }
            }
        }
        return dp[m][n];
    }
}