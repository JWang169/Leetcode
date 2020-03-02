package algorithm;

public class LongestIncreasingContinuousSubsequence{
    public int longestIncreasingContinuousSubsequence(int[] A) {
        if(A == null || A.length == 0) return 0;
        int[] increase = new int[A.length];
        int[] decrease = new int[A.length];
        increase[0] = decrease[0] = 1; 
        int result = 1;
        int curMax = 1;
        for(int i = 1; i < A.length; i++){
            if(A[i - 1] < A[i]) increase[i] = increase[i - 1] + 1;
            else increase[i] = 1;
            if(A[i - 1] > A[i]) decrease[i] = decrease[i - 1] + 1;
            else decrease[i] = 1;
            curMax = Math.max(decrease[i], increase[i]);
            result = Math.max(curMax, result);
        }
        return result;
    }
    
    
    public static void main(String[] args) {
    	LongestIncreasingContinuousSubsequence lics = new LongestIncreasingContinuousSubsequence();
    	int[] A = [5, 4, 2, 1, 3];
    	int result = lics.longestIncreasingContinuousSubsequence(A);
    	System.out.println(result);
    }
    
    
}