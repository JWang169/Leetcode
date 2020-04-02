class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False 
        ss = [0, 0]
        ee = [0, 0]
        ps, pe = 0, 0
        
        while True:
            while ps < len(start) and start[ps] == "X":
                ps += 1 
            while pe < len(end) and end[pe] == "X":
                pe += 1 
            
            if ps >= len(start) and pe >= len(end):
                return True 
            if ps >= len(start) or pe >= len(end):
                return False 
            
            if start[ps] != end[pe]:
                return False             
            elif start[ps] == 'L' and ps < pe:
                return False 
            elif start[ps] == 'R' and ps > pe:
                return False 
            ps += 1 
            pe += 1
            
            # elif ps == len(start) or pe == len(start):
            #     while ps < len(start) and start[ps] == 'X':
            #         ps += 1
            #     while pe < len(end) and end[pe] == 'X':
            #         pe += 1
            #     return ps == pe

 