class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not words[0]:
            return []
        
        result = []
        n = len(words[0])
        wordDict = {}
        for word in words:
            if len(word) != n:
                return []
            wordDict[word] = wordDict.get(word, 0) + 1
        

        for i in range(len(s) - len(words) * n + 1):
            sDict = {}
            valid = True
            for j in range(len(words)):
                sub = s[i + n * j: i + n * j + n]
                if sub not in wordDict:
                    valid = False
                    break
                else:
                    sDict[sub] = sDict.get(sub, 0) + 1
            
            
            for sub, count in sDict.items():
                if count != wordDict[sub]:
                    valid = False
                    break
            if valid:
                result.append(i)
        return result