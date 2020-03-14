"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque 
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        mappings = dict()
        nodeSet = set()
        queue = deque([node])
        while queue:
            n = queue.popleft()
            nodeSet.add(n)
            mappings[n.val] = Node(n.val)
            curNeighbors = n.neighbors
            for nei in curNeighbors:
                if nei not in nodeSet:
                    queue.append(nei)
        for n in nodeSet:
            val = n.val 
            neighs = n.neighbors 
            for nei in neighs:
                newNode = mappings[val]
                newNeighbor = mappings[nei.val]
                newNode.neighbors.append(newNeighbor)
        return mappings[node.val]
            