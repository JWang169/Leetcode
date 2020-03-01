public class MaximalSquare{
    /**
     * @param matrix: a matrix of 0 and 1
     * @return: an integer
     */
    public int maxSquare(int[][] matrix) {
        if(matrix == null || matrix.length == 0) return 0;
        
        int [][] count = new int[matrix.length][matrix[0].length];
        int i = 0, j = 0, result = 0;
        for(i = 0; i < matrix.length; i++){
            for(j = 0; j < matrix[0].length; j++){
                if(i == 0 || j == 0 || matrix[i][j] == 0){
                    count[i][j] = matrix[i][j];
                    result = Math.max(result, count[i][j]);
                    continue;
                }
                int prevCount = Math.min(count[i - 1][j], count[i][j - 1]);
                prevCount = Math.min(prevCount, count[i - 1][j - 1]);
                count[i][j] = prevCount + 1;
                result = Math.max(result, count[i][j]);
            }
        }
        return result * result;
    }
}