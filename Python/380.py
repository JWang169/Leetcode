class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.nums = list()
        self.size = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.data:
            return False
        self.nums.append(val)
        self.data[val] = self.size 
        self.size += 1
        return True 
        
    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.data:
            return False
        
        idx = self.data[val]
        del self.data[val]
        self.size -= 1
        
        if idx < self.size:
            self.nums[idx] = self.nums[-1]
            self.data[self.nums[-1]] = idx 
        self.nums.pop()
        return True 

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, self.size - 1)
        return self.nums[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()