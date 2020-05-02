class TinyUrl2:
    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def __init__(self):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.longURL = {}
        self.shortURL = {}
        
        
    def createCustom(self, long_url, key):
        if "http://tiny.url/" + key in self.shortURL and self.shortURL["http://tiny.url/" + key ] != long_url:
            return "error"
        if long_url in self.longURL and self.longURL[long_url] != "http://tiny.url/" + key:
            return "error"
        self.longURL[long_url] = "http://tiny.url/" + key
        self.shortURL["http://tiny.url/" + key] = long_url
        return "http://tiny.url/" + key
        

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        if long_url in self.longURL:
            return self.longURL[long_url]
        
        short = self.generate();
        while short in self.shortURL:
            short = self.generate()
        
        self.longURL[long_url] = short 
        self.shortURL[short] = long_url
    
        return short
        
        

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        # write your code here

        if short_url in self.shortURL:
            return self.shortURL[short_url]
        return None 
    
    
    def generate(self):
        import random
        short = ''
        for i in range(6):
            short += random.choice(self.chars)
        return  "http://tiny.url/" + short