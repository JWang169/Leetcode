class Codec:
    def encode(self, strs: [str]) -> str:
        result = ""
        for s in strs:
            result = result + str(len(s)) + ":" + s    
        return result
        
        
    def decode(self, s: str) -> [str]:
        strs = []
        while s:
            i = s.find(":")
            length = int(s[:i])
            s = s[i + 1:]
            strs.append(s[:length])
            s = s[length:]
        return strs
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))