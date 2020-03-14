"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        nodes, indegree = self.getGraph(graph)
        queue = deque()
        for node in nodes.keys():
            if node not in indegree:
                queue.append(node)
        results = list()
        while queue:
            node = queue.popleft()
            results.append(node)
            if node in nodes:
                children = nodes[node]
                for child in children:
                    indegree[child] -= 1 
                    if indegree[child] == 0:
                        queue.append(child)
        return results
        
        
        
    def getGraph(self, graph):
        nodes = dict()
        indegree = dict()
        for node in graph:
            ns = node.neighbors
            nodes[node] = nodes.get(node, set())
            for nei in ns:
                if nei not in nodes[node]:
                    nodes[node].add(nei)
                    indegree[nei] = indegree.get(nei, 0) + 1 
        return nodes, indegree