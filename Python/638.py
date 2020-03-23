class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.result = sys.maxsize
        self.dfs(price, special, needs, 0)
        return self.result
    
    def dfs(self, price, specials, needs, cost):
        if self.checkNeeds(needs):
            self.result = min(self.result, cost)
            return 
        if cost > self.result:
            return 
        for special in specials:
            newNeeds = []
            for i in range(len(needs)):                
                if needs[i] < special[i]:
                    break
                need = needs[i] - special[i] 
                newNeeds.append(need)
            if len(newNeeds) == len(needs):
                self.dfs(price, specials, list(newNeeds), cost+special[-1])
        
        for i in range(len(price)):
            cost += needs[i] * price[i]
        self.result = min(self.result, cost)
    
    def checkNeeds(self, needs):
        for need in needs:
            if need != 0:
                return False
        return True