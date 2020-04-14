class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        self.seen = dict()
        coins.sort()
        result = self.dfs(amount, coins, 0)
        return result
        
    
    def dfs(self, target, coins, idx):
        if (target, idx) in self.seen:
            return self.seen[(target, idx)]
        
        if target < 0:
            return 0
    
        if target == 0:
            return 1

        count = 0    
        for i in range(idx, len(coins)):
            if target - coins[i] < 0:
                break
            count += self.dfs(target - coins[i], coins, i)
            
        self.seen[(target, idx)] = count
        return count
        