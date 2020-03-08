
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = str

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add_word(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_word = True
        node.word = word

class Solution:
    """
    @param words: a set of stirngs
    @param target: a target string
    @param k: An integer
    @return: output all the strings that meet the requirements
    """
    def kDistance(self, words, target, k):
        trie = Trie()
        for word in words:
            trie.add_word(word)
        
        n = len(target)
        dp = [i for i in range(n + 1)]
        result = []
        
        self.find(trie.root, target, k, dp, result)
        return result
    
    def find(self, node, target, k, dp, result):
        n = len(target)
        if node.is_word:
            print(node.word, dp[n])
        if node.is_word and dp[n] <= k:
            result.append(node.word)
            
        next = [0 for i in range(n + 1)]
        for c in node.children:
            next[0] = dp[0] + 1
            for i in range(1, n + 1):
                if target[i - 1] == c:
                    # print(target[i - 1], c)
                    next[i] = min(dp[i - 1], min(dp[i] + 1, next[i - 1] + 1))
                else:
                    next[i] = min(dp[i - 1] + 1, dp[i] + 1, next[i - 1] + 1)
            
            self.find(node.children[c], target, k, next, result)