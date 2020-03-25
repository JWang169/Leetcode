class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None 
        
    
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.nums = [None] * self.size 
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashKey = self.hashfunc(key)
        node = ListNode(key, value)
        head = self.nums[hashKey]
        if head:
            node.next = head
        self.nums[hashKey] = node 
        
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashKey = self.hashfunc(key)
        head = self.nums[hashKey]
        while head:
            if head.key == key:
                return head.val
            head = head.next
        return -1 
        
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashKey = self.hashfunc(key)
        head = self.nums[hashKey]
        prev = None
        while head:
            if head.key == key:
                if prev:
                    prev.next = head.next
                    head = head.next
                else:
                    self.nums[hashKey] = head.next
                    head = head.next
            else:
                prev = head
                head = head.next
            
                    
                                
    def hashfunc(self, key):
        return key % self.size 
        
        

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)