class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.count = n 
        self.graph = dict()
    
    def connect(self, a, b):
        rootA = self.find(a)
        rootB = self.find(b)
        if rootA != rootB:
            self.count -= 1 
            self.graph[rootA] = rootB

    """
    @return: An integer
    """
    def query(self):
        return self.count 
        
    def find(self, a):
        if a not in self.graph:
            self.graph[a] = a 
            return a
        paths = []
        while self.graph[a] != a:
            paths.append(a)
            a = self.graph[a]
        for p in paths:
            self.graph[p] = a 
        return a 