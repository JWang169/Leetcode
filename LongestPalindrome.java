package algorithm;
import java.util.*;

public class LongestPalindrome {
	
	public int longestPalindrome(String s) {
		
		HashMap<Character, Integer> map = new HashMap<>();
		
		for(Character ch: s.toCharArray()) {
			if(map.containsKey(ch)) {
				map.put(ch, map.get(ch) + 1);
			}else{
				map.put(ch, 1);
			}
		}
		
		int result = 0;
		boolean odd = false;
		
		for(Character key: map.keySet()) {
			if(map.get(key) % 2 == 0) result += map.get(key);
			else {
				odd = true;
				result += map.get(key) - 1;
			}
		}
		
		if(odd) result ++;
		return result;	

	}
	
	
	public static void main(String[] args) {
		LongestPalindrome lp = new LongestPalindrome();
		String s1 = "abccccdd";
		String s2 = "";
		System.out.println(lp.longestPalindrome(s1));
		System.out.println(lp.longestPalindrome(s2));
		
	}

}


