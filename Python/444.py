from collections import deque
class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        if not seqs:
            return not org
        graph, indegree = self.buildGraph(seqs)
        queue = deque()
        for n in graph.keys():
            if n not in indegree:
                queue.append(n)
        results = []
        while len(queue) == 1:
            cur = queue.popleft()
            results.append(cur)
            if cur in graph:
                children = graph[cur]
                for child in children:
                    indegree[child] -= 1 
                    if indegree[child] == 0:
                        queue.append(child)
        return results == org and len(results) == len(graph)
        
        
    def buildGraph(self, seqs):
        graph = dict()
        indegree = dict()
        for seq in seqs:
            for i in range(len(seq)):
                if i == len(seq) - 1:
                    graph[seq[i]] = graph.get(seq[i], set())
                    continue
                graph[seq[i]] = graph.get(seq[i], set())
                if seq[i + 1 ] not in graph[seq[i]]:
                    graph[seq[i]].add(seq[i + 1])
                    indegree[seq[i + 1]] = indegree.get(seq[i + 1], 0) + 1
            
        return  graph, indegree