public class CourseSchedule {
    /*
     * @param numCourses: a total of n courses
     * @param prerequisites: a list of prerequisite pairs
     * @return: true if can finish all courses or false
     */
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[][] pres = prerequisites;
        if(numCourses == 0 || pres == null || pres.length == 0) return true;
        
        //1. build graph
        Map<Integer, ArrayList<Integer>> graph = new HashMap<>();
        int[] degree = new int[numCourses];
        
        for(int i = 0; i < numCourses; i++){
            graph.put(i, new ArrayList<Integer>());
        }
        
        for(int i = 0; i < pres.length; i++){
            graph.get(pres[i][1]).add(pres[i][0]);
            //2. build indegree 
            degree[pres[i][0]]++;
        }
        
        
        //3. add 0 degree to queue
        int count = 0;
        Queue<Integer> queue = new LinkedList<>();
        for(int i = 0; i < numCourses; i++){
            if(degree[i] == 0) {
                queue.add(i);
                count++;
            }
        }
        
        //4. bfs
        
        while(!queue.isEmpty()){
            int course = queue.poll();
            if(graph.get(course) != null){
                for (int n: graph.get(course)){
                    degree[n]--;
                    if(degree[n] == 0){
                        queue.offer(n);
                        count++;
                    }
                }
            }
        }
        return count == numCourses;
    }
}