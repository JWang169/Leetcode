class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        move = 0 
        # left: -1, right: 1 
        for direction, amount in shift:
            x = direction if direction == 1 else -1
            move += x * amount 
        
        move = move % len(s)
        return s[-move: ] + s[:-move]
        
        
        
        