class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        self.results = []
        sub = []
        self.dfs(s, sub, 0)
        return self.results 
        
    def dfs(self, s, prev, start):
        if start == len(s):
            self.results.append(prev)
            return 
        self.dfs(s, prev + [s[start: start + 1]], start + 1)
        if start < len(s) - 1:
            self.dfs(s, prev + [s[start: start + 2]], start + 2)