class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.results = []
        self.dfs(word, 0, 0)
        return self.results
        
    def dfs(self, word, i, num):
        if i == len(word):
            self.results.append(word)
            return 
        
        if num == 0:
            abbr = word[:i] + "1" + word[i + 1:]
            self.dfs(abbr, i + 1, 1)
            self.dfs(word, i + 1, 0)
        else:
            # skip next char:
            self.dfs(word, i + 1, 0)
            # abbreviate next char
            len_num = len(str(num))
            left = i - len_num
            abbr = word[: left] + str(num + 1) + word[i + 1:]
            idx = len(word[:left] + str(num + 1))
            self.dfs(abbr, idx, num + 1)
                
            
        
        
        
        