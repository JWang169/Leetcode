class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        val1 = 0
        for n1 in num1:
            val = ord(n1) - ord('0')
            val1 = val1 * 10 + val 
            
        val2 = 0
        for n2 in num2:
            val = ord(n2) - ord('0')
            val2 = val2 * 10 + val 
        
        return str(val1 + val2)