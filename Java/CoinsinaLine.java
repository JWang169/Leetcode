public class CoinsinaLine.java {
    /**
     * @param n: An integer
     * @return: A boolean which equals to true if the first player will win
     */
    public boolean firstWillWin(int n) {
        // write your code here
        if(n == 0) return false;
        if(n == 1 || n == 2) return true;
        boolean[] leftCoins = new boolean[n + 1];
        leftCoins[0] = false;
        leftCoins[1] = leftCoins[2] = true;
        for(int i = 3; i <= n; i++){
            leftCoins[i] = !leftCoins[i - 1] || !leftCoins[i - 2];
        }
        return leftCoins[n];
    }
}