public class MinPathSum{
	public int minPathSum(int[][] grid) {
        // write your code here
        if(grid == null || grid.length == 0) return 0;
        int[][] sums = new int[grid.length][grid[0].length];
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(i == 0 && j == 0) sums[i][j] = grid[i][j];
                else if(i == 0) sums[i][j] = sums[i][j - 1] + grid[i][j];
                else if(j == 0) sums[i][j] = sums[i - 1][j] + grid[i][j];
                else{
                    sums[i][j] = Math.min(sums[i - 1][j], sums[i][j - 1]) + grid[i][j];
                }
            }
        }
        return sums[grid.length - 1][grid[0].length - 1];
    }
}