class GeoHash:
    """
    @param: latitude: one of a location coordinate pair 
    @param: longitude: one of a location coordinate pair 
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        chars = "0123456789bcdefghjkmnpqrstuvwxyz"
        latBin = self.getBin(latitude, -90, 90)
        logBin = self.getBin(longitude, -180, 180)
        
        hashCode, b = '', ''
        
        for i in range(30):
            b += logBin[i] + latBin[i] 
        

        for i in range(0, 60, 5):
            hashCode += chars[int(b[i: i + 5], 2)]
        
        return hashCode[:precision]
        
        
    def getBin(self, target, left, right):
        b = ''
        for i in range(30):
            mid = (left + right) / 2.0
            if target > mid:
                left = mid
                b += '1'
            else:
                right = mid 
                b += '0'
        return b 
        
        