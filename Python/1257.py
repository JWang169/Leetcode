class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        seen = set()
        graph = {}
        for nodes in regions:
            root = nodes[0]
            if root not in graph:
                graph[root] = root
            for child in nodes[1:]:
                graph[child] = root

        paths1 = self.search(region1, graph)
        paths2 = self.search(region2, graph)
        
        length = min(len(paths1), len(paths2))
        index = length
        
        for i in range(length):
            if paths1[i] != paths2[i]:
                index = i
                break
        return paths1[index - 1]
        
    def search(self, region, graph):
        paths = []
        root = region
        while graph[root] != root:
            paths.append(root)
            root = graph[root]
        paths.append(root)
        return paths[::-1]
        
            