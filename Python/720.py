class Solution:
    def longestWord(self, words: List[str]) -> str:
        mappings = collections.defaultdict(list)
        for word in words:
            mappings[len(word)].append(word)
        lens = sorted(mappings.keys())
        i = 1
        trie = {}
        if 1 not in mappings:
            return None
        else:
            result = mappings[1][0]
            
        while i in mappings:
            if i == 1:
                for word in mappings[1]:
                    trie[word] = {}
                i += 1
                continue
            cur = mappings[i]
            for word in cur:
                level = trie
                valid = True 
                for j in range(len(word) - 1):
                    if word[j] in level:
                        level = level[word[j]]
                    else:
                        valid = False 
                if valid:
                    level[word[-1]] = {}
                    if len(word) == len(result):
                        result = min(result, word)
                    else:
                        result = word
                
            i += 1 
        return result
                
        