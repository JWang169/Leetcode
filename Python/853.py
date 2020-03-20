class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        mappings = {}
        for i in range(len(position)):
            mappings[position[i]] = speed[i]
        
        pos = sorted(mappings.keys(), reverse=True)
        times = []
        count = 0
        
        for car in pos:
            time = (target - car) / mappings[car]
            if not times or times[-1] < time:
                times.append(time)
                count += 1 
        
        return count