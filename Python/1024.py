class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        end, end2, res = -1, 0, 0
        for i, j in sorted(clips):
            if end2 >= T or i > end2:
                break
            if end < i <= end2:
                res += 1 
                end = end2
            end2 = max(end2, j)
        return res if end2 >= T else -1
        
        