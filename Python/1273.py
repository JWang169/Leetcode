# update the value from children to root
# for loop should start from the leaf node, instead of the root node 
# This is from lee215. Very smart solution
class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        res = [1] * nodes
        for i in range(nodes - 1, 0, -1):
            p = parent[i]
            v = value[i]
            # update parent value
            value[p] += v
            # update the number of child nodes. if current v != 0, the parent will have one more child.
            res[p] += res[i] if v != 0 else 0
        return res[0]
        
        
        



#  TLE
class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """
        def buildGraph():
            graph = dict()
            for i in range(nodes):
                p = parent[i]
                graph[p] = graph.get(p, set())
                graph[p].add(i)
            return graph 
        
        def getPath(x):
            path = []
            while parent[x] != -1:
                path.append(x)
                x = parent[x]
            path.append(0)
            return path
        
        sums = dict()
        graph = buildGraph()
        for i in range(nodes):
            path = getPath(i)
            v = value[i]
            for p in path:
                sums[p] = sums.get(p, 0) + v
        
        # print(sums)
        stack = []
        for i in range (nodes):
            if sums[i] == 0:
                stack.append(i)

        removed = set()
        count = 0
        while stack:
            cur = stack.pop()
            if cur not in removed:
                removed.add(cur)
                count += 1 
            if cur in graph:
                for child in graph[cur]:
                    stack.append(child)

        return nodes - count
                
        
        
        
        