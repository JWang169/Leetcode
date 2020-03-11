public class Solution {
    /**
     * @param nums: A list of integers
     * @param k: An integer
     * @return: The median of the element inside the window at each moving
     */
    
    PriorityQueue <Integer> maxHeap, minHeap;
    public List<Integer> medianSlidingWindow(int[] nums, int k) {
        List <Integer> res = new ArrayList<>();
        int n = nums.length;
        if(n == 0){
            return res;
        }
        maxHeap = new PriorityQueue<Integer>(n, Collections.reverseOrder());
        minHeap = new PriorityQueue<Integer>(n);
        
        int i; 
        for(i = 0; i < n; i++){
            if(maxHeap.size() == 0 || nums[i] <= maxHeap.peek()){
                maxHeap.offer(nums[i]);
            }
            else{
                minHeap.offer(nums[i]);
            }
            balance();
            if(i - k >= 0){
                if(nums[i - k] > maxHeap.peek()){
                    minHeap.remove(nums[i - k]);
                }
                else{
                    maxHeap.remove(nums[i - k]);
                }
            }
            balance();
            if(i >= k - 1){
                res.add(maxHeap.peek());
            }
            
        }
        
        return res;
    }
    private void balance(){
        while (maxHeap.size() < minHeap.size()){
            maxHeap.offer(minHeap.poll());
        }
        while (minHeap.size() < maxHeap.size() - 1){
            minHeap.offer(maxHeap.poll());
        }
    }
    
}