class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {']': '[', '}': '{', ')': '('}
        stack = []
        for ss in s:
            if ss in pairs:
                if len(stack) == 0:
                    return False 
                if stack.pop() != pairs[ss]:
                    return False
            else:
                stack.append(ss)
        return len(stack) == 0