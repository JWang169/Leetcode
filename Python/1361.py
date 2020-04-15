class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = dict()
        count = 0
        def find(u):
            if u not in graph:
                graph[u] = u
                return u
            while u != graph[u]: 
                u = graph[u]
            return u
        
                
        for i in range(n):
            root_i = find(i)
            if leftChild[i] != -1:
                left = leftChild[i]
                root_left = find(left)
                if root_left != left:
                    return False    
                if root_left == root_i:
                    return False 
                count += 1 
                graph[root_left] = root_i
            
            if rightChild[i] != -1:
                right = rightChild[i]
                root_right = find(right)
                if root_right != right:
                    return False 
                if root_right == root_i:
                    return False 
                count += 1 
                graph[root_right] = root_i
        return count == n - 1
        
        