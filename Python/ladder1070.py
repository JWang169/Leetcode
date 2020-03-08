from collections import defaultdict
class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        self.graph = dict()
        n = len(accounts)
        for i in range(n):
            self.graph[i] = i
            
        self.buildGraph(accounts)
        
        idToEmail = defaultdict(set)
        for i in range(len(accounts)):
            superId = self.find(i)
            emails = accounts[i][1:]
            for email in emails:
                idToEmail[superId].add(email)
                
        results = []
        for id, emails in idToEmail.items():
            emails = sorted(list(emails))
            results.append([accounts[id][0]] + emails)
        return results
    
    
    def buildGraph(self, accounts):
        self.emailToId = defaultdict(list)
        for id, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                self.emailToId[email].append(id)
        
        for email, ids in self.emailToId.items():
            rootId = ids[0]
            for id in ids[1:]:
                self.union(id, rootId)
               
                
    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        self.graph[rootU] = rootV
    
    
    def find(self, a):
        paths = []
        while self.graph[a] != a:
            a = self.graph[a]
            paths.append(a)
        for p in paths:
            self.graph[p] = a 
        return a 
        