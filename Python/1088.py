class Solution:
    def confusingNumberII(self, N: int) -> int:
        self.nums = {0 : 0, 1 : 1, 6 : 9, 8 : 8, 9 : 6}
        self.count = 0
        self.dfs(0, 0, 1, N)
        return self.count 
    
    def dfs(self, origin, rotation, digit, N):
        if origin != rotation:
            self.count += 1 
        
        for key, val in self.nums.items():
            # add one digit to origin
            if key == 0 and origin == 0:
                continue
            if origin * 10 + key > N:
                continue
            else:
                self.dfs(origin * 10 + key, rotation + val * digit, digit * 10, N)
    



# Time Limit Exceeded
# class Solution:
#     def confusingNumberII(self, N: int) -> int:
#         nums = {0 : 0, 1 : 1, 6 : 9, 8 : 8, 9 : 6}
#         count = 0
#         for i in range(N+1):
#             if self.isValid(i, nums):
#                 count += 1 
#         return count 
    
    
#     def isValid(self, i, nums): 
#         oldNum = i
#         digits = []
#         while i > 0:
#             digit = i % 10 
#             if digit not in nums:
#                 return False 
#             digits.append(nums[digit])
#             i = i // 10 
#         newNum = 0
#         for digit in digits:
#             newNum = newNum * 10 + digit
#         if newNum != oldNum:
#             return True
#         return False 