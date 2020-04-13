class LogSystem:
    
    def __init__(self):
        self.history = dict()
                

    def put(self, id: int, timestamp: str) -> None:
        nums = timestamp.split(":")
        self.history[tuple(nums)] = id
        

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        ss = s.split(':')
        ee = e.split(':')
        mappings = {'Year': 0, 'Month': 1, 'Day': 2, 'Hour': 3, 'Minute':4, 'Second': 5}
        idx = mappings[gra]
        start = "".join(ss[:idx + 1])
        end = "".join(ee[:idx + 1])
        result = []
        for key, val in self.history.items():
            if start <= "".join(key[:idx + 1]) <= end:
                result.append(val)
        return result
            
            
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)