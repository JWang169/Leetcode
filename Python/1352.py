class ProductOfNumbers(object):

    def __init__(self):
        self.nums = []
        self.prods = []
        self.zero = -sys.maxsize 
        self.index = -1
    def add(self, num):
        """
        :type num: int
        :rtype: None
        """
        self.index += 1 
        if num == 0:
            self.zero = self.index 
            num = 1 
        if self.index == 0:
            self.prods.append(num)
        else:
            self.prods.append(num * self.prods[-1])
        
    

    def getProduct(self, k):
        """
        :type k: int
        :rtype: int
        """

        left = self.index - k
        if self.zero > left:
            return 0
        if left < 0:
            return self.prods[-1]
        return self.prods[-1] / self.prods[left]
        
        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)