class Solution:
    
    
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.results = []
        self.dfs(digits, "", 0)
        return self.results
        
    def dfs(self, digits, prev, start):
        if start == len(digits):
            self.results.append(prev)
            return 
        mappings = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        letters = mappings[digits[start]]
        for letter in letters:
            self.dfs(digits, prev + letter, start + 1)
        return 
    
            