class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        n = len(indexes)
        changes = []
        for i in range(n):
            idx = indexes[i]
            source = sources[i]
            target = targets[i]
            m = len(source)
            if S[idx: idx + m] != source:
                continue
            changes.append([idx, idx + m, target])
        
        left = 0
        result = ""
        changes.sort()
        for start, end, target in changes:
            result = result + S[left : start] + target
            left = end
        result += S[left:]
        return result 
            