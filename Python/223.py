class Solution:
    """
    两个矩形=> 先坐标排序！使两者位置固定！
    """
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        # sum(rectangles) - overlap
        
        points = [((A, B), (C, D)), ((E, F), (G, H))]
        points.sort()
        ((A, B), (C, D)), ((E, F), (G, H)) = points
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        
        overlap = 0
        x = min(C, G) - E
        y = min(D, H) - max(B, F)
        
        if x > 0 and y > 0:
            overlap = x * y
        return area1 + area2 - overlap
        