class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        pairs = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        result = [] 
        for pair in pairs:
            height = pair[1]
            if len(result) == 0 or height > result[-1]:
                result.append(height)
            else:
                index = bisect.bisect_left(result, height)
                result[index] = height 
        return len(result)
                