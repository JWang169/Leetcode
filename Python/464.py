# 不你没背下来 April 8 你又写错了
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        self.seen = {}
        nums = [i for i in range(1, maxChoosableInteger + 1)]
        if sum(nums) < desiredTotal:
            return False 
        return self.dfs(nums, desiredTotal)        
            
    
    def dfs(self, nums, remain):
        if tuple(nums) in self.seen:
            return self.seen[tuple(nums)]

        key = tuple(nums)
        if nums and nums[-1] >= remain:
            self.seen[key] = True 
            return True
    
        if not nums and remain > 0:
            return False 
        
        for i in range(len(nums)):
            if not self.dfs(nums[:i] + nums[i + 1:], remain - nums[i]):
                self.seen[key] = True
                return True
        
        self.seen[key] = False
            
        return self.seen[key]
    


 # April 4 写了两次，差不多背下来了
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}
        def dfs(nums, target):
            key = tuple(nums)
            if key in seen:
                return seen[key]
            if nums[-1] >= target:
                seen[key] = True
                return True 
            for i in range(len(nums)):
                # 如果下一个status是False, 那current就是True
                if not dfs(nums[:i] + nums[i + 1:], target - nums[i]):
                    seen[key] = True 
                    return True 
            seen[key] = False
            return False 
        
        nums = [i for i in range(1, maxChoosableInteger + 1)]
        if sum(nums) < desiredTotal:
            return False 
        return dfs(nums, desiredTotal)
        
        

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}
        
        def dfs(choices, remain):
            # if the greatest choice exceeds the remain: win
            if choices[-1] >= remain:
                return True 
            
            cur = tuple(choices)
            
            # if we have seen this senario: return the result 
            if cur in seen:
                return seen[cur]
            
            for i in range(len(choices)):
                if not dfs(choices[:i] + choices[i + 1:], remain - choices[i]):
                    seen[cur] = True 
                    return True 
                
            seen[cur] = False 
            return False 
        
        choices = []
        for i in range(1, maxChoosableInteger + 1):
            choices.append(i)
        if sum(choices) < desiredTotal:
            return False 
        
        return dfs(choices, desiredTotal)
            
            
        
        