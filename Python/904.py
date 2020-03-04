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