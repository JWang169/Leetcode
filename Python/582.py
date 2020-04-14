class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        graph = collections.defaultdict(set)
        for idx, num in enumerate(pid):
            parent = ppid[idx]
            graph[parent].add(num)
        results = []
        queue = deque([kill])
        while queue:
            cur = queue.popleft()
            results.append(cur)
            if cur not in graph:
                continue
            for child in graph[cur]:
                queue.append(child)
        return results
            
        
        
        