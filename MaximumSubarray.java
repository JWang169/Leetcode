public class MaximumSubarray {
    /**
     * @param nums: A list of integers
     * @return: A integer indicate the sum of max subarray
     */
    public int maxSubArray(int[] nums) {
        // write your code here
        if(nums == null || nums.length == 0) return 0;
        int[] cumsum = new int[nums.length];
        cumsum[0] = nums[0];
        int result = cumsum[0];
        for(int i = 1; i < nums.length; i++){
            if(cumsum[i - 1] < 0) cumsum[i] = nums[i];
            else{
                cumsum[i] = cumsum[i - 1] + nums[i];
            }
            result = Math.max(cumsum[i], result);
        }
        return result;
    }
}