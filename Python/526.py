class Solution:
    def countArrangement(self, N: int) -> int:
        nums = set([i for i in range(1, N + 1)])
        self.result = 0
        print(nums)
        self.dfs(nums, 1)
        return self.result
    
    def dfs(self, nums, idx):
        if not nums:
            self.result += 1 
            return 
        for num in nums:
            if num % idx == 0 or idx % num == 0:
                nums.remove(num)
                self.dfs(set(nums), idx + 1)
                nums.add(num)
        
        