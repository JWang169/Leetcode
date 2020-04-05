class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        letters = []
        if a > 0:
            letters.append([a, 'a'])
        if b > 0:
            letters.append([b, 'b'])
        if c > 0:
            letters.append([c, 'c'])
        res = ""
        while True:
            if not letters:
                break
            letters.sort()
            # print(letters)
            if len(res) > 1 and res[-1] == res[-2] == letters[-1][1]:
                if len(letters) == 1:
                    break
                res += letters[-2][1]
                letters[-2][0] -= 1 
              
            else:
                res += letters[-1][1]
                letters[-1][0] -= 1    
            newLetters = []
            for num, ch in letters:
                if num == 0:
                    continue
                newLetters.append([num, ch]) 
            letters = newLetters
            
        return res 
        
        
        