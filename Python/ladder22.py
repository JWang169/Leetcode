from collections import deque
class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if not nestedList:
            return []
        queue = deque(nestedList)
        results = []
        while queue:
            cur = queue.popleft()
            if isinstance(cur, list):
                while cur:
                    queue.appendleft(cur.pop())
            else:
                results.append(cur)
        return results 
                    