class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        seqs = [lower - 1] + nums + [upper + 1]
        res = []
        
        for i in range(len(seqs) - 1):
            if seqs[i + 1] - seqs[i] == 2:
                res.append(str(seqs[i + 1] - 1))
            elif seqs[i + 1] - seqs[i] > 2:
                res.append(str(seqs[i] + 1) + "->" + str(seqs[i + 1] - 1))
        return res 