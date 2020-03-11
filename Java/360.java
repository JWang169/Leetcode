class Solution {
    PriorityQueue<Integer> maxHeap, minHeap;
    public double[] medianSlidingWindow(int[] nums, int k) {
        
        int n = nums.length;
        double[] results = new double[n - k + 1];
        if(n == 0){
            return null;
        }
        maxHeap = new PriorityQueue<Integer>(n, Collections.reverseOrder());
        minHeap = new PriorityQueue<Integer>(n);
    
        for(int i = 0; i < n; i++){
            if(maxHeap.size() == 0 || nums[i] <= maxHeap.peek()){
                maxHeap.offer(nums[i]);
            }
            else{
                minHeap.offer(nums[i]);
            }
            balance();
            
            if(i >= k){
                if(nums[i - k] > maxHeap.peek()){
                    minHeap.remove(nums[i - k]);
                }
                else{
                    maxHeap.remove(nums[i - k]);
                }
            }
            balance();
            double mid;
            if(maxHeap.size() > minHeap.size()){
                mid = (double) maxHeap.peek();
            }
            else{
                mid = (double) ((long)maxHeap.peek() + (long)minHeap.peek()) / 2;
            }
            if(i >= k - 1){
                results[i - k + 1] = mid;
            }
        }
        return results;
    }
    
    private void balance(){
        while(minHeap.size() > maxHeap.size()){
            maxHeap.offer(minHeap.poll());
        }
        while(minHeap.size() < maxHeap.size() - 1){
            minHeap.offer(maxHeap.poll());
        }
    }
}