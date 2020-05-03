'''
Definition of Trip:
class Trip:
    self.id; # trip's id, primary key
    self.driver_id, self.rider_id; # foreign key
    self.lat, self.lng; # pick up location
    def __init__(self, rider_id, lat, lng):

Definition of Helper
class Helper:
    @classmethod
    def get_distance(cls, lat1, lng1, lat2, lng2):
        # return calculate the distance between (lat1, lng1) and (lat2, lng2)
'''
from Trip import Trip, Helper


class MiniUber:

    def __init__(self):
        self.drivers = {}
        self.trips = {}


    # @param {int} driver_id an integer
    # @param {double} lat, lng driver's location
    # return {trip} matched trip information if there have matched rider or null
    def report(self, driver_id, lat, lng):
        if driver_id not in self.trips:
            self.drivers[driver_id] = (lat, lng)
            return None 
        
        trip = self.trips[driver_id]
        # trip.lat = lat
        # trip.lng = lng 
        return trip 
    
        
        
    # @param rider_id an integer
    # @param lat, lng rider's location
    # return a trip
    def request(self, rider_id, lat, lng):
        trip = Trip(rider_id, lat, lng)
        mi = sys.maxsize
        driverId = None 
        
        for driver in self.drivers.keys():
            driverLat, driverLng = self.drivers[driver]
            dist = Helper.get_distance(lat, lng, driverLat, driverLng)
            if dist < mi:
                driverId = driver 
                mi = dist 
        
        if driverId:
            del self.drivers[driverId]
        
        trip.driver_id = driverId 
        self.trips[driverId] = trip 
        return trip 
  
                
                
        