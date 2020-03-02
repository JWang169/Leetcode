public class LongestContinuousIncreasingSubsequenceII {
    /**
     * @param matrix: A 2D-array of integers
     * @return: an integer
     */
    int[] dx = {-1, 1, 0, 0};
    int[] dy = {0, 0, -1, 1};
    int[][] dp;
    int m, n;
    
    public int longestContinuousIncreasingSubsequence2(int[][] matrix) {
        // write your code here
        if(matrix.length == 0) return 0;
        n = matrix.length;
        m = matrix[0].length;
        int result = 0;
        dp = new int[n][m]; //dp[i][j] means the longest continuous increasing 
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                search(i, j, matrix);
                result = Math.max(result, dp[i][j]);
            }
        }
        return result;
    }
    
    public void search(int x, int y, int[][] matrix){
        if(dp[x][y] != 0) return;
        int nx, ny;
        dp[x][y] = 1;
        for(int i = 0; i < 4; i++){
            nx = x + dx[i];
            ny = y + dy[i];
            if(nx >= 0 && nx < n && ny >= 0 && ny < m){
                if(matrix[nx][ny] > matrix[x][y]){
                    search(nx, ny, matrix);
                    dp[x][y] = Math.max(dp[x][y], dp[nx][ny] + 1);
                }
            }
        }
    }
}