class Solution:
    def similarRGB(self, color: str) -> str:
        hexes = {'a': 10, 'b': 11, 'c':12, 'd': 13, 'e': 14, 'f': 15}
        for i in range(10):
            hexes[str(i)] = i
            
        result = "#"
        for i in range(1, 4):
            h0 = color[i * 2 - 1]
            h1 = color[i * 2]
            num = hexes[h0] * 16 + hexes[h1] 
            diff = sys.maxsize 
            for key, val in hexes.items():
                target = val * 16 + val
                if abs(target - num) < diff:
                    replace = key * 2
                    diff = abs(target - num)
            result += replace
            
        return result
            