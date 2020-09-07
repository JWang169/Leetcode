class Solution:
    def getInterval(self, active):
        interval = 0
        x_left = 0
        for x1, x2 in active:
            x_left = max(x_left, x1) 
            interval += max(0, x2 - x_left)
            x_left = max(x_left, x2)
            
        return interval

    
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        # line sweep => in and out
        events = []

        for x1, y1, x2, y2 in rectangles:
            events.append((y1, 0, x1, x2))
            events.append((y2, 1, x1, x2))
        events.sort()
        
        active = []
        cur_y = events[0][0]
        res = 0
        for y, state, x1, x2 in events:
            res += self.getInterval(active) * (y - cur_y)
            if state == 0:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
            
            cur_y = y
        
        return res % (10**9 + 7)
        
        