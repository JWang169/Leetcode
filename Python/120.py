class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        prev = triangle[0]
        for i in range(1, len(triangle)):
            row = triangle[i]
            cur = [0] * len(row)
            for j in range(len(row)):
                if j == 0:
                    cur[j] = prev[j] + row[j]
                    continue 
                if j == len(row) - 1:
                    cur[j] = prev[j - 1] + row[j]
                    continue
                cur[j] = min(prev[j - 1], prev[j]) + row[j]
            prev = cur 
        return min(prev)
                    