class Solution:
    def decodeString(self, s: str) -> str:
        self.stack = []
        number = 0
        for i in range(len(s)):
            if s[i] == '[':
                self.stack.append(number)
                number = 0
            if s[i] == ']':
                self.helper()
            if s[i].isalpha():
                self.stack.append(s[i])
                
            if s[i].isdigit():
                number *= 10
                number += int(s[i])
        
        return ''.join(self.stack)
        
    def helper(self):
        subStack = []
        chars = ''
        while isinstance(self.stack[-1], str):
            subStack.append(self.stack.pop())
        num = self.stack.pop() 
        baseStr = ''
        while subStack:
            baseStr += subStack.pop()
        for i in range(num):
            self.stack.append(baseStr)
