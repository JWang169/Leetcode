class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a = 0
        b = 0
        degreeSecret = [0] * 10
        degreeGuess = [0] * 10
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a += 1 
            else:
                degreeSecret[int(secret[i])] += 1 
                degreeGuess[int(guess[i])] += 1
        
        for i in range(10):
            b += min(degreeSecret[i], degreeGuess[i])
        return str(a) + 'A' + str(b) + 'B'
            
                