class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        chars = "0123456789bcdefghjkmnpqrstuvwxyz"
        b = ""
        
        for ch in geohash:
            # find the index of ch in chars
            idx = chars.find(ch)
            b += self.idx2binary(idx)
        
        odd = ''.join([b[i] for i in range(0, len(b), 2)])
        even = ''.join([b[i] for i in range(1, len(b), 2)])
        
        location = []
        location.append(self.getLocation(-90, 90, even))
        location.append(self.getLocation(-180, 180, odd))
        return location 
        
        
    def idx2binary(self, idx):
        b = ''
        for i in range(5):
            if idx % 2 == 0:
                b = '0' + b
            else:
                b = '1' + b 
            idx //= 2 
        return b 
        
    
    def getLocation(self, start, end, string):
        for ch in string:
            mid = (start + end) / 2 
            if ch == '1':
                start = mid 
            else:
                end = mid 
        return (start + end) / 2
        
