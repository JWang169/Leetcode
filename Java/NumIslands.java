public class NumIslands{
    /**
     * @param grid: a boolean 2D matrix
     * @return: an integer
     */
    public int numIslands(boolean[][] grid) {
        // write your code here
        if(grid == null || grid.length == 0) return 0;
        int result = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j]){
                    grid[i][j] = false;
                    search(i, j, grid);
                    result += 1;
                }
            }
        }
        return result;
    }
    private void search(int x, int y, boolean[][]grid){
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        for(int i = 0; i < 4; i++){
            int nx = dx[i] + x;
            int ny = dy[i] + y;
            if(nx >= 0 && nx < grid.length && ny >= 0 && ny < grid[0].length && grid[nx][ny]){
                grid[nx][ny] = false;
                search(nx, ny, grid);
            }
        }
    }
}