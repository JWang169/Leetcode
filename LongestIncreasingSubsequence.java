public class LongestIncreasingSubsequence {
    /**
     * @param nums: An integer array
     * @return: The length of LIS (longest increasing subsequence)
     */
    public int longestIncreasingSubsequence(int[] nums) {
        // write your code here
        if(nums == null || nums.length == 0) return 0;
        int result = 1;
        int n = nums.length;
        int[] f = new int[n];
        for(int i = 0; i < n; i++){
            f[i] = 1;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    f[i] = Math.max(f[j] + 1, f[i]);
                }
            }
            result = Math.max(result, f[i]);
        }
        return result;
    }
}