'''
Definition of Location:
class Location:
    # @param {double} latitude, longitude
    # @param {Location}
    @classmethod
    def create(cls, latitude, longitude):
        # This will create a new location object

Definition of Restaurant:
class Restaurant:
    # @param {str} name
    # @param {Location} location
    # @return {Restaurant}
    @classmethod
    def create(cls, name, location):
        # This will create a new restaurant object,
        # and auto fill id

Definition of Helper
class Helper:
    # @param {Location} location1, location2
    @classmethod
    def get_distance(cls, location1, location2):
        # return calculate the distance between two location

Definition of GeoHash
class GeoHash:
    # @param {Location} location
    # @return a string
    @classmethom
    def encode(cls, location):
        # return convert location to a geohash string
    
    # @param {str} hashcode
    # @return {Location}
    @classmethod
    def decode(cls, hashcode):
        # return convert a geohash string to location
'''
from YelpHelper import Location, Restaurant, GeoHash, Helper


class MiniYelp:

    def __init__(self):
        self.restaurants = {}
        


    # @param {str} name
    # @param {Location} location
    # @return {int} restaurant's id
    def add_restaurant(self, name, location):
        r = Restaurant.create(name, location)
        self.restaurants[r.id] = r 
        return r.id 


    # @param {int} restaurant_id
    # @return nothing
    def remove_restaurant(self, restaurant_id):
        if restaurant_id in self.restaurants:
            del self.restaurants[restaurant_id]
        return 
    

    # @param {Location} location
    # @param {double} k, distance smaller than k miles
    # @return {str[]} a list of restaurant's name and sort by 
    # distance from near to far.
    def neighbors(self, location, k):
        nearby = []
        for id, res in self.restaurants.items():
            loc1 = res.location
            dist = Helper.get_distance(loc1, location)
            if dist < k:
                nearby.append((dist, res.name))
        nearby.sort()
        result = []
        for n in nearby:
            result.append(n[1])
        return result
                
        
        
        
        