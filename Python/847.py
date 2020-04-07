class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        final = "1" * n 
        queue = deque()
        seen = set()
        for i in range(n):
            tag = ["0"] * n
            tag[i] = "1"
            # number, step, states
            queue.append((i, 0, "".join(tag)))
        
        while queue:
            for i in range(len(queue)):
                num, step, state = queue.popleft()
                if state == final:
                    return step
                
                for n in graph[num]:
                    # print("n: ", n)
              
                    newState = state[:n] + "1" + state[n + 1:]
                    # print('newState: ', newState)
                    if (n, newState) not in seen:
                        queue.append((n, step + 1, newState))
                        seen.add((n, newState))

        
        
        