from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        seqs = dict()
        visited = set(["0000"])
        for i in range(1, 9):
            seqs[str(i)] = [str(i - 1), str(i + 1)]
        seqs['0'] = ['1', '9']
        seqs['9'] = ['8', '0']
        queue = deque()
        queue.append("0000")
        count = -1
        while queue:
            count += 1 
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == target:
                    return count 
                if cur in deadends:
                    continue
                for i in range(4):
                    for j in range(2):
                        nxt = cur[:i] + seqs[cur[i]][j] + cur[i + 1:]
                        if nxt not in visited:
                            visited.add(nxt)
                            queue.append(nxt)
            
        return -1
                        
            
        