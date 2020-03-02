public class HouseRobber{
    /**
     * @param A: An array of non-negative integers
     * @return: The maximum amount of money you can rob tonight
     */
    public long houseRobber(int[] A) {
        // write your code here
        if(A == null || A.length == 0) return 0;
        if(A.length == 1) return A[0];
        if(A.length == 2) return Math.max(A[0], A[1]);
        long[] income = new long[A.length];
        income[0] = A[0];
        income[1] = Math.max(A[0], A[1]);
        for(int i = 2; i < A.length; i++){
            income[i] = Math.max(A[i] + income[i - 2], income[i - 1]);
        }
        return income[A.length - 1];
    }
}