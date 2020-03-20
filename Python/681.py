class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = set()
        for digit in time:
            if digit.isdigit():
                digits.add(int(digit))
        digits = list(digits)
        
        hourStr, minStr = time.split(":")
        oldH, oldMin = int(hourStr), int(minStr)
        minMin = 59
        ansMin = 59
        foundMin = False
        for n1 in digits:
            for n2 in digits:
                newMin = n1 * 10 + n2
                if newMin < 60 and newMin > oldMin:
                    foundMin = True 
                    ansMin = min(newMin, ansMin)
                if newMin < minMin:
                    minMin = newMin
        
        ansMin = self.format(ansMin)
        minMin = self.format(minMin)
        
        if foundMin:
            return hourStr + ":" + ansMin
          
        foundH = False
        ansH = 23
        minH = 23
        
        for n1 in digits:
            for n2 in digits:
                newH = n1 * 10 + n2
                if newH < 24 and newH > oldH:
                    foundH = True
                    ansH = min(ansH, newH)      
                minH = min(minH, newH)
                
        ansH = self.format(ansH)
        minH = self.format(minH)
        if foundH:
            return ansH + ":" + minMin
        else:
            return minH + ":" + minMin
        
        
    def format(self, num):
        return '0' + str(num) if num < 10 else str(num)