class UndergroundSystem:

    def __init__(self):
        self.history = collections.defaultdict(dict)
        self.idToStation = dict()
        self.stationTostation = collections.defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.history[stationName][id] = t           
        self.idToStation[id] = stationName
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.idToStation[id] 
        startTime = self.history[startStation][id]
        self.stationTostation[startStation][stationName] = self.stationTostation[startStation].get(stationName, [])
        self.stationTostation[startStation][stationName].append(t - startTime)
        
        
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return mean(self.stationTostation[startStation][endStation])


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)