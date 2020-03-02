public class CoinsinaLineII {
    /**
     * @param values: a vector of integers
     * @return: a boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int[] values) {
        // write your code here
        if(values == null || values.length == 0) return false;
        int n = values.length;
        int[] f = new int[n + 1];
        f[n] = 0;
        f[n - 1] = values[n - 1];
        for(int i = n - 2; i >= 0; i--){
            f[i] = Math.max(values[i] - f[i + 1], values[i] + values[i + 1] - f[i + 2]);
        }
        return f[0] > 0;
    }
}