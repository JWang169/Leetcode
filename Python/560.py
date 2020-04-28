class Solution(object):
    def subarraySum(self, nums, k):
        presums = []
        result = 0
        total = 0
        visited = {0: 1}
        for i in range(len(nums)):
            total += nums[i]
            target = total - k
            if target in visited:
                result += visited[target]
            
            visited[total] = visited.get(total, 0) + 1
            
        return result