class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        res = ""
        for i in itertools.permutations(arr):
            i = map(str, i)
            cur = ''.join(i)
            if cur[:2] < "24" and cur[2:4] < "60":
                if not res:
                    res = cur
                else:
                    res = max(res, cur)
        if not res:
            return ""
        return res[:2] + ':' + res[2:]