class ConnectingGraph2:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.graph = {}
        self.count = [1] * (n + 1)

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.graph[rootA] = rootB
            self.count[rootB] += self.count[rootA]
        
        
    """
    @param: a: An integer
    @return: An integer
    """
    def query(self, a):
        # write your code here
        return self.count[self.find(a)]

    
    def find(self, a):
        if a not in self.graph:
            self.graph[a] = a 
            return a 
        paths = []
        while a != self.graph[a]:
            paths.append(a)
            a = self.graph[a]
        for path in paths:
            self.graph[path] = a 
        return a 