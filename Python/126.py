from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        letters = "abcdefghijklmnopqrstuvwxyz"
        results = []
        queue = deque()
        queue.append([beginWord])
        found = False
        while queue:
            for i in range(len(queue)):
                words = queue.popleft()
                curWord = words[-1]
                if curWord == endWord:
                    found = True
                    results.append(words)
                    continue
                if curWord in wordSet:
                    wordSet.remove(curWord)
                for i in range(len(curWord)):
                    for letter in letters:
                        newWord = curWord[:i] + letter + curWord[i + 1:]
                        if newWord in wordSet:
                            queue.append(words + [newWord])
            if found:
                return results
        return []