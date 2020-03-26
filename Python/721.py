class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.graph = dict()
        n = len(accounts)
        for i in range(n):
            self.graph[i] = i
        
        self.buildGraph(accounts)
        idToEmail = collections.defaultdict(set)
        for id, account in enumerate(accounts):
            rootId = self.find(id)
            for email in account[1:]:
                idToEmail[rootId].add(email)
        results = []
        for i, emails in idToEmail.items():
            name = accounts[i][0]
            results.append([name] + sorted(list(emails)))
    
        return results
            
    
    def buildGraph(self, accounts): 
        emailToId = collections.defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emailToId[email].append(i)
                
        for email, ids in emailToId.items():
            rootId = ids[0]
            for id in ids[1:]:
                self.union(id, rootId)
    
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        self.graph[rootU] = rootV
    
    
    def find(self, u):
        paths = []
        while self.graph[u] != u:
            paths.append(u)
            u = self.graph[u]
            
        for path in paths:
            self.graph[path] = u
        return u
    