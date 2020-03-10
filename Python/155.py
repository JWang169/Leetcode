class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
            return 
        prev = self.minStack[-1]
        if x < prev:
            self.minStack.append(x)
        else:
            self.minStack.append(prev)
        return 

    def pop(self) -> None:
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()