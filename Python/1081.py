class Solution:
    def smallestSubsequence(self, text: str) -> str:
        last = {}
        for i, c in enumerate(text):
            last[c] = i
        
        stack = []
        for i, c in enumerate(text):
            if c in stack:
                continue 

            while stack and stack[-1] > c and last[stack[-1]] > i:
                stack.pop()
            stack.append(c)
        
        return "".join(stack)n