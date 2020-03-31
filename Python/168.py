class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        while n > 0:
            remain = (n - 1) % 26
            letter = chr(65 + remain) 
            result += letter
            n = (n - 1) // 26

        return result[::-1]
        