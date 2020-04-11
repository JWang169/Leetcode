class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort()
        n = len(arr)
        left = 0
        right = arr[-1]
        while left + 1 < right:
            mid = (left + right) // 2
            cur = self.getSum(arr, mid)
            # print("mid, cur: ", mid, cur)
            if cur > target:
                right = mid 
            elif cur < target:
                left = mid 
            else:
                return mid
            # print('left, right: ', left, right)
        # print(left, right)
        sumLeft = self.getSum(arr, left)
        sumRight = self.getSum(arr, right)
        if abs(sumLeft - target) > abs(sumRight - target):
            return right
        return left
        
        
    
    def getSum(self, arr, mid):
        cumsum = 0
        n = len(arr)
        for i in range(n):
            if arr[i] < mid:
                cumsum += arr[i]
            else:
                cumsum += (n - i) * mid
                break
        return cumsum 
        
        
        