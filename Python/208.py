class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False 
    
    
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self.trie
        for ch in word: 
            if ch not in root.children:
                node = Node()
                root.children[ch] = node 
            root = root.children[ch]
        root.isWord = True
        return 
                    

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.trie
        for letter in word:
            if letter not in root.children:
                return False 
            root = root.children[letter]
        if root.isWord:
            return True 
        else:
            return False 
        
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.trie
        for letter in prefix:
            if letter not in root.children:
                return False 
            root = root.children[letter]
        
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)