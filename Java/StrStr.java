public class StrStr {
    /**
     * @param source: 
     * @param target: 
     * @return: return the index
     */
    public int strStr(String source, String target) {
        // Write your code here
        if(target == null || source == null) return -1;
        if(target.length() == 0) return 0;
        for(int i = 0; i < source.length() - target.length() + 1; i++){
            int j = 0;
            int idx = i;
            while(idx < source.length() && j < target.length()){
                if(source.charAt(idx) == target.charAt(j)){
                    idx++; 
                    j++;
                }
                else break;
            } 
            if(j == target.length()) return i;
        }
        return -1;
    }
}