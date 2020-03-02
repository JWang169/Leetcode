public class MaxProductSubarray{
    /**
     * @param nums: An array of integers
     * @return: An integer
     */
    public int maxProduct(int[] nums) {
        // write your code here
        if(nums == null || nums.length == 0) return 0;
        int[] neg = new int[nums.length];
        int[] pos = new int[nums.length];
        neg[0] = pos[0] = nums[0];
        int result = nums[0];
        for(int i = 1; i < nums.length; i++){
            pos[i] = Math.max(nums[i], Math.max(pos[i - 1] * nums[i], neg[i - 1] * nums[i]));
            neg[i] = Math.min(nums[i], Math.min(pos[i - 1] * nums[i], neg[i - 1] * nums[i]));
        
            result = Math.max(result, Math.max(pos[i], neg[i]));
        }
        return result;
        
    }
}