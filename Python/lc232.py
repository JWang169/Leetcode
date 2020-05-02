class TinyUrl:
    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def __init__(self):
        self.chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.longURL = {}
        self.shortURL = {}
    
    
    def longToShort(self, url):
        if url in self.longURL:
            return self.longURL[url]
        shorten = self.generateShort(url)
        # 去重， 如果见过了就重新再生成一次
        while shorten in self.shortURL:
            shorten = self.generateShort(url)
        self.longURL[url] = shorten
        self.shortURL[shorten] = url 
        return shorten
        

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        if url in self.shortURL:
            return self.shortURL[url]
        return None 
    
    def generateShort(self, url):
        import random 
        shorten = ''
        for i in range(6):
            shorten += random.choice(self.chars)
        return 'http://tiny.url/' + shorten
        
        
