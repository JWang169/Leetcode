package algorithm;

public class BurstBalloon {
	public int maxCoins(int[] nums) {
		int n = nums.length;
		if(n == 0) return 0;
		int i, j, k, len;
		int[] A = new int[n + 2];
		A[0] = A[n + 1] = 1;
		for(i = 1; i <=n; i++) {
			A[i] = nums[i - 1];
		}
		n += 2;
		int[][] f = new int[A.length][A.length];
		// if length == 2, two adjacent balloons cannot burst
		for(i = 0; i < A.length - 1; i++) {
			f[i][i + 1] = 0;
		}
		
		//length
		
		for(len = 3; len <= A.length; len++) {
			//start position i, end position: j, length: len
			// balloon i and j cannot burst
			// the maximum score will be in [i+1, i+2 ... j-1]	
			for(i=0; i <= A.length - len; i++) {
				j = i + len - 1;
				f[i][j] = 0;
				//last balloon to break between i and j: k;
				for(k = i + 1; k < j; k++) {
					f[i][j] = Math.max(f[i][j], f[i][k] + f[k][j] + A[i] * A[j] * A[k]);
				}
			}
			
		}
		return f[0][A.length - 1];
	}
	public static void main(String[] args) {
		BurstBalloon bb = new BurstBalloon();
		int[] nums1 = new int[] {3,1,5};
		int[] nums2 = new int[] {4, 1, 5, 10};
		int result1 = bb.maxCoins(nums1);
		int result2 = bb.maxCoins(nums2);
		System.out.println(result1);
		System.out.println(result2);
	}

}
