public class Solution {
    /**
     * @param height: A list of integer
     * @return: The area of largest rectangle in the histogram
     */
    public int largestRectangleArea(int[] height) {
        if(height == null || height.length == 0){
            return 0;
        }
        int area = 0;
        Stack<Integer> stack = new Stack<Integer>();
        int max = 0;
        for(int i = 0; i <= height.length; i++){
            int curt = (i == height.length) ? -1 : height[i];
            while(!stack.isEmpty() && curt <= height[stack.peek()]){
                int h = height[stack.pop()];
                int left = stack.isEmpty() ? 0 : (stack.peek() + 1);
                int right = i - 1;
                area = Math.max(area, h * (right - left + 1));
                
            }
            stack.push(i);
        }
        return area;
    }
}