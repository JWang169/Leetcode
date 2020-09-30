"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

from collections import deque
class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        queue = deque()
        people = dict()
        for person in employees:
            cur_id, cur_imp, cur_sub = person.id, person.importance, person.subordinates
            people[cur_id] = [cur_sub, cur_imp]
        
        queue.append(id)
        res = 0
        seen = set()
        while queue:
            cur = queue.pop()
            res += people[cur][1]
            for nxt in people[cur][0]:
                if nxt not in seen:
                    queue.append(nxt)
        return res 