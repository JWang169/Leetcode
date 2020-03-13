class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        left, right = 0, len(arr) - 1 
        while left + 1 < right:
            mid = (left + right) // 2
            if arr[mid] > x:
                right = mid
            else:
                left = mid
        if abs(arr[left] - x) <= abs(arr[right] - x):
            center = left
        else:
            center = right 
        k -= 1 
        results = [arr[center]]
        left = center - 1
        right = center + 1 
        while k > 0:
            k -= 1
            if left < 0:
                results.append(arr[right])
                right += 1
                continue
            if right >= len(arr):
                results.append(arr[left])
                left -= 1
                continue
            if abs(arr[left] - x) <= abs(arr[right] - x):
                results.append(arr[left])
                left -= 1
            else:
                results.append(arr[right])
                right += 1 
        
        return sorted(results)