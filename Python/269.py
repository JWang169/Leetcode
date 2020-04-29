class Solution:
    def alienOrder(self, words: List[str]) -> str:        
        graph = dict()
        indegree = dict()
        
        for word in words:
            for ch in word:
                graph[ch] = graph.get(ch, set())
        
        for i, word in enumerate(words):
            if i == 0:
                continue
            prev = words[i - 1]
            
            found = False
            for j in range(len(word)):
                if j == len(prev):
                    found = True
                    break
                    
                if prev[j] == word[j]:               
                    continue
                
                found = True
                if word[j] not in graph[prev[j]]:
                    graph[prev[j]].add(word[j])
                    indegree[word[j]] = indegree.get(word[j], 0) + 1
                break
            if not found and prev != word:
                return ""
            
            
        queue = deque()
        for ch in graph.keys():
            if ch not in indegree:
                queue.append(ch)
        
        result = ""
        while queue:
            cur = queue.popleft()
            result += cur 
            if cur not in graph:
                continue
            children = graph[cur]
            for child in children:
                if child in indegree:
                    indegree[child] -= 1 
                    if indegree[child] == 0:
                        queue.append(child)
                        del indegree[child]
        
        if len(indegree) == 0:
            return result
        return ""
                
                
                
        