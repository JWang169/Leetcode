class Codec:
    def __init__(self):
        self.dic = {}
        self.dic2 = {}
    
    
    def encode(self, longUrl: str) -> str:
        self.dic[longUrl] = str(random.randint(1, 100))
        self.dic2["http://tinyurl.com/" + self.dic[longUrl]] = longUrl
        return "http://tinyurl.com/" + self.dic[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.dic2[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))