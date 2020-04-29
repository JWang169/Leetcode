class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = 0
        for ch in s:
            if ch == '[':
                stack.append(number)
                number = 0
                continue
            if ch == ']':
                chars = []   
                while stack:
                    letter = stack.pop()
                    if isinstance(letter, int):
                        num = letter
                        break
                    chars.append(letter)
                
                newString = ""
                while chars:
                    newString += chars.pop()
                stack.append(newString * num)
                        
            if ch.isalpha():
                stack.append(ch)
            if ch.isdigit():
                number *= 10
                number += int(ch)
            

        res = ""
        stack = stack[::-1]
        while stack:
            res += stack.pop()
        return res


    
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
