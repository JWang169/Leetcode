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
            
            
        
        