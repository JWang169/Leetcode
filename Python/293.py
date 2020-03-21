class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        results = []
        for i in range(len(s) - 1):
            if s[i: i + 2] == "++":
                results.append(s[:i] + "--" + s[i + 2:])
        return results