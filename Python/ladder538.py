class Cookie:
    def __init__(self, time, value, ttl):
        self.start = time 
        self.ttl = ttl
        self.value = value 
        

class Memcache:
    def __init__(self):
        self.graph = dict()
        self.na = 2147483647
        

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.graph:
            return self.na 
        cookie = self.graph[key]
        if cookie.ttl == 0 or curtTime - cookie.start < cookie.ttl:
            return cookie.value 

        return self.na 

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        cookie = Cookie(curtTime, value, ttl)
        self.graph[key] = cookie 
        return 
        

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key in self.graph:
            del self.graph[key]
        return 


    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if key not in self.graph:
            return self.na 
        cookie = self.graph[key]
        if curtTime - cookie.start < cookie.ttl or cookie.ttl == 0:
            cookie.value += delta 
            return cookie.value 
        return self.na 
        
        

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        if key not in self.graph:
            return self.na 
        cookie = self.graph[key]
        if curtTime - cookie.start < cookie.ttl or cookie.ttl == 0:
            cookie.value -= delta 
            return cookie.value       
        return self.na