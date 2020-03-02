public class ScrambleString {
    /**
     * @param s1: A string
     * @param s2: Another string
     * @return: whether s2 is a scrambled string of s1
     */
    public boolean isScramble(String s1, String s2) {
        // write your code here
        if(s1.equals(s2)) return true;
        if(s1.length() != s2.length()) return false;
        char[] t1 = s1.toCharArray();
        char[] t2 = s2.toCharArray();
        Arrays.sort(t1);
        Arrays.sort(t2);
        for(int i = 0; i < t1.length; i++){
            if (t1[i] != t2[i]) return false; 
        }
        
        for(int i = 1; i < t1.length; i++){
            boolean result = (isScramble(s1.substring(0, i), s2.substring(0, i))
                            && isScramble(s1.substring(i), s2.substring(i))) 
                            || (isScramble(s1.substring(0, i), s2.substring(s2.length() - i))
                            && isScramble(s1.substring(i), s2.substring(0, s2.length() - i)));
            if(result) return true;
            
        }
        return false;
    }
}