class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:  
        
        if n <= 1:
            return 0
        total = 0
        told = set([headID])
        graph = collections.defaultdict(list)
        for idx, source in enumerate(manager):
            graph[source].append(idx)
        
        q = deque([(headID, informTime[headID])])
        while q:
            id, time = q.popleft()
            total = max(total, time)
            for child in graph[id]:
                if child not in told:
                    told.add(child)
                    q.append((child, time + informTime[child]))
            if len(told) == n:  
                return total
        