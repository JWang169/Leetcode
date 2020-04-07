class TrieNode():
    def __init__(self):
        self.children = {}
        self.weights = []

class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, i):
        node = self.root
        node.weights.append(i)
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.weights.append(i)
    
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.weights
        
class WordFilter:
    def __init__(self, words: List[str]):
        self.prefix, self.suffix = Trie(), Trie()
        i, n = 0, len(words)
        while i < n:
            w = words[i]
            self.prefix.insert(w, i)
            self.suffix.insert(w[::-1], i)
            i += 1

    def f(self, prefix: str, suffix: str) -> int:
        pre = self.prefix.search(prefix)
        suf = self.suffix.search(suffix[::-1])
        i, j = len(pre) - 1, len(suf) - 1
        while i >= 0 and j >= 0:
            if pre[i] == suf[j]:
                return pre[i]
            elif pre[i] < suf[j]:
                j -= 1
            else:
                i -= 1
        return -1


# 有bug
"""
class Node:
    def __init__(self, weight):
        self.next = {}
        self.weights = [weight]
        
    
class WordFilter:

    def __init__(self, words: List[str]):
        self.prefix = self.getPrefix(words)
        self.suffix = self.getSuffix(words)
    
    def getPrefix(self, words):
        prefix = Node(0)
        for i, word in enumerate(words):
            prev = prefix
            for ch in word:
                if ch in prev.next:
                    prev = prev.next[ch]
                    prev.weights.append(i)
                else:
                    prev.next[ch] = Node(i)
                    prev = prev.next[ch]
        return prefix  
    
    
    def getSuffix(self, words):
        suffix = Node(0)
        for i, word in enumerate(words):
            suf = suffix
            for ch in word[::-1]:
                if ch in suf.next:
                    suf = suf.next[ch]
                    suf.weights.append(i)
                else:
                    suf.next[ch] = Node(i)
                    suf = suf.next[ch]

        return suffix
        

    def f(self, prefix: str, suffix: str) -> int:
        weightPre = self.search(prefix, 'pref')
        weightSuf = self.search(suffix, 'surf')
        setP = set(weightPre)

        for s in weightSuf[::-1]:
            if s in setP:
                return s
        return -1 
            
    
    def search(self, sub, tag):
        if tag == "pref":
            trie = self.prefix
        else:
            trie = self.suffix
            sub = sub[::-1]
        
        result = []
        for ch in sub:
            if ch not in trie.next:
                return []
            trie = trie.next[ch]
            result = trie.weights
        return result
"""                  
    

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)