class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        # map x to y 
        xx = collections.defaultdict(set) 
        # map y to x
        yy = collections.defaultdict(set) 
        for x, y in points:
            xx[x].add(y)
            yy[y].add(x)
        
        area = sys.maxsize
        
        for x0, y0 in points:
            if len(xx[x0]) < 2 or len(yy[y0]) < 2:
                continue
                
            for y1 in xx[x0]:
                if y1 == y0:
                    continue
                xs = yy[y1]
                for x1 in xs:
                    if x1 != x0 and x1 in yy[y0]:
                        area = min(area, abs(x0 - x1) * abs(y0 - y1))
                        
        if area != sys.maxsize:
            return area
        return 0
        
        
        