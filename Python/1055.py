class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        mappings = dict()
        for idx, letter in enumerate(source):
            mappings[letter] = mappings.get(letter, [])
            mappings[letter].append(idx)
        
        i, j = 0, 0
        count = 1
        while i < len(target):
            if target[i] not in mappings:
                return -1

            idxs = mappings[target[i]]
            found = False
            for idx in idxs:
                if idx >= j:
                    j = idx + 1 
                    i += 1 
                    found = True 
                    break
            if not found:
                j = 0
                count += 1 
        
        return count 
            
            
                    