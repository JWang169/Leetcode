# Apr 12
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        left = 0
        result = 0
        seen = dict()
        cur = 0
        for i, n in enumerate(tree):
            seen[n] = seen.get(n, 0) + 1
            if len(seen) <= 2:
                result = max(result, i - left + 1)
                cur += 1 
                continue 
            while len(seen) > 2:
                seen[tree[left]] -= 1 
                if seen[tree[left]] == 0:
                    del seen[tree[left]]
                left += 1 
        return result 
            


class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        result = 0
        start = 0
        types = dict()
        for i in range(len(tree)):
            types[tree[i]] = types.get(tree[i], 0) + 1 
            while len(types) > 2:
                types[tree[start]] -= 1
                if types[tree[start]] == 0:
                    del types[tree[start]]
                start += 1 
            result = max(result, i - start + 1)
        return result