class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            target = words[i]
            cols = ""
            for row in words:
                if len(row) > i:
                    cols += row[i]
            if target != cols:
                return False 
        return True 
                    