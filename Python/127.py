from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words:
            return 0
        count = 0
        queue = deque()
        queue.append(beginWord)
        alpha = "abcdefghijklmnopqrstuvwxyz"
        while queue:
            count += 1 
            for _ in range(len(queue)):
                curWord = queue.popleft()
                if curWord == endWord:
                    return count
                for i in range(len(curWord)):
                    for ch in alpha:
                        newWord = curWord[:i] + ch + curWord[i + 1:] 
                        if newWord in words:
                            queue.append(newWord)   
                            words.remove(newWord)
                            
        return 0