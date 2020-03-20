class ListNode:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000000
        self.nums = [None] * self.size
        

    def add(self, key: int) -> None:
        if self.contains(key):
            return 
        hashKey = self.hashfunc(key)
        newNode = ListNode(key, None)
        if self.nums[hashKey] == None:
            self.nums[hashKey] = newNode
        else:
            self.nums[hashKey].next = newNode
        

    def remove(self, key: int) -> None:
        hashKey = self.hashfunc(key)
        node = self.nums[hashKey]
        prev = None
        while node:
            if node.val == key:
                nxt = node.next 
                if prev:
                    prev.next = nxt 
                    return 
                else:
                    self.nums[hashKey] = nxt
                    return 
            else:
                node = node.next 
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        hashKey = self.hashfunc(key)
        node = self.nums[hashKey]
        while node:
            if node.val == key:
                return True 
            else:
                node = node.next 
        return False    
        
    
    def hashfunc(self, num):
        hashKey = num % self.size        
        return hashKey


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)