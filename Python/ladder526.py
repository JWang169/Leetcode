# 要点是删除即把数组中最后一个元素放到删除的元素的位置
import random
class LoadBalancer:
    def __init__(self):
        self.idx = -1
        self.servers = dict()
        self.nums = []

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        if server_id not in self.servers:
            self.idx += 1 
            self.servers[server_id] = self.idx
            self.nums.append(server_id)
            
 
    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id in self.servers:
            replace = self.servers[server_id]
            self.nums[replace] = self.nums[self.idx]
            self.servers[self.nums[self.idx]] = replace
            
            del self.servers[server_id]
            self.nums.pop()
            
            
            self.idx -= 1 
             
        

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        idx = random.randint(0, self.idx)
        return self.nums[idx]
        
        