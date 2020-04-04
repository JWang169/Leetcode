class StringIterator:

    def __init__(self, compressedString: str):
        self.queue = deque()
        self.pairs = None
        i = 0
        cur = ""
        while i < len(compressedString):
            ch = compressedString[i]
            if ch.isalpha():
                cur = ch
                i += 1 
                continue
            num = 0
            while i < len(compressedString) and compressedString[i].isdigit():
                num = num * 10 + int(compressedString[i])
                i += 1
            self.queue.append([cur, num])
        print(self.queue)
        
    def next(self) -> str:
        if not self.hasNext():
            return ' '
        if not self.pairs:
            self.pairs = self.queue.popleft()
        ch = self.pairs[0]
        self.pairs[1] -= 1 
        if self.pairs[1] == 0:
            self.pairs = None
        return ch
                

    def hasNext(self) -> bool:
        return len(self.queue) > 0 or self.pairs


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()