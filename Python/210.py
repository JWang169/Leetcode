from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = dict()
        indegree = dict()
        for c0, c1 in prerequisites:
            indegree[c0] = indegree.get(c0, 0) + 1
            graph[c1] = graph.get(c1, set())
            graph[c1].add(c0)
        
        queue = deque()
        for i in range(numCourses):
            if i not in indegree:
                queue.append(i)
        results = []
        while queue:
            c = queue.popleft()
            results.append(c)
            if c in graph:
                children = graph[c]
                for child in children:
                    indegree[child] -= 1 
                    if indegree[child] == 0:
                        queue.append(child)
            
        if len(results) == numCourses:
            return results
        else:
            return []