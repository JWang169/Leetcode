package algorithm;

public class DecodeWays {
	public int numDecodings(String s) {
		
		int[] results = new int[s.length() + 1];
		if(s.charAt(0) == '0') return 0;
		results[0] = results[1] = 1;
		for(int i = 2; i <= s.length(); i++) {
			if(s.charAt(i - 1) != '0') results[i] = results[i - 1];
			int twoDigits = (s.charAt(i - 2) - '0') * 10 + s.charAt(i - 1) - '0';
			if(twoDigits >= 10 && twoDigits <= 26) {
				results[i] += results[i - 2];
			}
		}
		
		return results[s.length()];
	}
	
	public static void main(String[] args) {
		String s = "10";
		DecodeWays dw = new DecodeWays();
		int res = dw.numDecodings(s);
		System.out.println(res);
	}
}
