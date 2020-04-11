class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0] * n
        stack = []
        for log in logs:
            id, event, time = log.split(':')
            if event == 'start':
                if stack:
                    prevId, prevTime = stack[-1]
                    result[prevId] += int(time) - prevTime
                stack.append([int(id), int(time)])
            else:
                prev = stack.pop()
                result[prev[0]] += int(time) - prev[1] + 1
                if stack:
                    stack[-1][1] = int(time) + 1           
                
        return result
        
        
        