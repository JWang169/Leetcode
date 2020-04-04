class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        length = sys.maxsize
        result = None 
        letters = collections.defaultdict()
        for letter in licensePlate:
            if letter.isalpha():
                letter = letter.lower()
                letters[letter] = letters.get(letter, 0 ) + 1 
        
        for word in words:
            cur = collections.Counter(word)
            valid = True 
            for letter in letters:
                if letter not in cur or cur[letter] < letters[letter]:
                    valid = False 
                    break
            if valid and len(word) < length:
                result = word
                length = len(word)
                    
        return result
        
        
        