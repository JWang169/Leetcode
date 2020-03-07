class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        # do intialization if necessary
        self.graph = dict()
        
    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        rootA = self.search(a)
        rootB = self.search(b)
        self.graph[rootA] = rootB


    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        rootA = self.search(a)
        rootB = self.search(b)
        return rootA == rootB
        
    
    def search(self, a):
        if a not in self.graph:
            self.graph[a] = a 
            return a 
        root = a 
        paths = []
        while self.graph[root] != root:
            root = self.graph[root]
        for path in paths:
            self.graph[path] = root
        return root 
            