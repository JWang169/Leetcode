class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # center of rectangle
        cx, cy = (x2 + x1) / 2, (y2 + y1) / 2
        dist = (x_center - cx) ** 2 + (y_center - cy) ** 2
        
        return dist <= (radius + (x2 - x1) / 2) ** 2 + ((y2 - y1) / 2) ** 2
        
        
        
        
        