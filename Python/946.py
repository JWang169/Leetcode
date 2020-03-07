class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        if not pushed and not popped:
            return True
        if len(pushed) != len(popped):
            return False 
        
        popIdx = 0
        count = 0
        stack = []
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while len(stack) > 0 and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1 
        return len(stack) == 0
            
            
        