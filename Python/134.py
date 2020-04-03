class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas:
            return -1
        if len(gas) == 1:
            return 0 if gas[0] >= cost[0] else -1
        pairs = []
        for i in range(len(gas)):
            pairs.append(gas[i] - cost[i])
        path = pairs + pairs
        n = len(gas)
        for i in range(len(gas)):
            presum = path[i]
            for j in range(i + 1, i + len(gas)):
                if presum < 0:
                    break
                presum += path[j]
            if j - i == len(gas) - 1 and presum >= 0:
                return i         
                
        return -1
            
        
        
        