import heapq
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}
        for idx, letter in enumerate(s):
            last[letter] = idx 
        
        stack = []
        
        for idx, letter in enumerate(s):
            if letter in stack:
                continue
            if not stack:
                stack.append(letter)
                continue 
            while stack and letter < stack[-1] and last[stack[-1]] > idx:
                stack.pop()
            stack.append(letter)
        return ''.join(stack)