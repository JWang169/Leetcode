class Solution:
    def findComplement(self, num: int) -> int:
        b = bin(num)
        output = ""
        for char in b[2:]:
            output += '1' if char == '0' else '0'
        return int(output, 2)
        