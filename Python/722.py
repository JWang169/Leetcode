class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        comment = False
        cur = ''
        for line in source:
            i = 0
            while i < len(line):
                if line[i: i + 2] == '//' and not comment:
                    break
                if line[i: i + 2] == '/*' and not comment:
                    comment = True 
                    i += 1
                elif line[i: i + 2] == '*/' and comment:
                    comment = False 
                    i += 1 
                elif not comment:
                    cur += line[i]
                i += 1 
            if cur and not comment:
                result.append(cur)
                cur = ''
        return result
                    
                    