"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

import collections
class Solution:
    """
    @param {UndirectedGraphNode[]} nodes a array of undirected graph node
    @return {int[][]} a connected set of a undirected graph
    """
    def connectedSet(self, nodes):
        self.graph = dict()
        visited = set()
        for node in nodes:
            self.graph[node.label] = self.graph.get(node.label, node.label)
            visited.add(node.label)
            for nei in node.neighbors:
                self.union(node.label, nei.label)
    
        result = dict()
        print(self.graph)
      
      
        for label in self.graph.keys():
            parent = self.find(label)
            if parent not in result:
                result[parent] = []
            result[parent].append(label)

        clusters = []
        for key, val in result.items():
            clusters.append(sorted(val))
        return clusters
            
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        self.graph[rootV] = rootU       
            
            
    
    def find(self, u):
        if u not in self.graph:
            self.graph[u] = u 
            return u
        paths = []
        while u != self.graph[u]:
            paths.append(u)
            u = self.graph[u]
        for p in paths:
            self.graph[p] = u
        return u 
        