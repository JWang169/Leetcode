class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        # worst case k ** n
        def dfs(cur, seen, total):
            if len(seen) == total:
                return cur
            for i in range(k):
                temp = cur[-n + 1: ] + str(i) if n != 1 else str(i)
                if temp not in seen:
                    seen.add(temp)
                    res = dfs(cur + str(i), seen, total)
                    if res:
                        return res
                    seen.remove(temp)
        return dfs("0" * n, set(["0" * n]), k**n)
    
    
    