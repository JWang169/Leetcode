class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        self.result = False
        self.dfs(nums)
        return self.result    
    
    def dfs(self, nums):
        # pick two numbers from the available numbers
        # do operation on these two 
        # add the result to the numbers list 
        # go to next iteration
        if len(nums) == 1:
            if abs(nums[0] - 24) <= 10e-5:
                self.result = True 
            return 
        
        pairs = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                a, b = nums[i], nums[j]
                newNums = []
                for k in range(len(nums)):
                    if k != i and k != j:
                        newNums.append(nums[k])
                results = self.operate(a, b)
                for result in results:
                    self.dfs(newNums + [result])
        return 
                
    def operate(self, a, b):
        results = []
        results.append(a + b)
        results.append(a - b)
        results.append(a * b)
        if b != 0:
            results.append(a / b)
        results.append(b - a)
        if a != 0:
            results.append(b / a)
        return results
        
