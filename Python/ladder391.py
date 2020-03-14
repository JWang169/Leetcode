"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        if not airplanes:
            return 0
            
        events = []
        for airplane in airplanes:
            start, end  = airplane.start, airplane.end
            events.append((start, 1))
            events.append((end, -1))
        
        events.sort()
        count = 0
        result = 0
        for event in events:
            count += event[1]
            result = max(count, result)
        return result
        
        
        