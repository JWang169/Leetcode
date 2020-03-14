from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = dict()
        pairs = dict()
        for c0, c1 in prerequisites:
            indegree[c0] = indegree.get(c0, 0) + 1 
            pairs[c1] = pairs.get(c1, set())
            pairs[c1].add(c0)
        
        queue = deque() 
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        
        count = 0
        while queue:
            count += 1 
            course = queue.popleft()
            if course in pairs:
                for child in pairs[course]:
                    indegree[child] -= 1 
                    if indegree[child] == 0:
                        queue.append(child)
        return count == numCourses