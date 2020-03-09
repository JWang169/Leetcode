"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        self.quickSelect(nuts, bolts, 0, len(nuts) - 1, compare.cmp)
        
    def quickSelect(self, nuts, bolts, start, end, cmp):
        if start >= end:
            return 

        idx = self.partition(bolts, start, end , nuts[(start + end)//2], cmp)
        self.partition(nuts, start, end , bolts[idx], cmp)
        
        self.quickSelect(nuts, bolts, start, idx-1, cmp)
        self.quickSelect(nuts, bolts, idx + 1, end, cmp)
    
    def partition(self, arr, start, end, pivot, cmp): 
        left, right = start, end 
        
        # find the num in arr equals to the pivot:
        for i in range(left, right + 1):
            # first assume arr is nuts and pivot is from bolts then the other way 
            if cmp(arr[i], pivot) == 0 or cmp(pivot, arr[i]) == 0:
                arr[i], arr[left] = arr[left], arr[i]
                left += 1
                break
        
        while left <= right:
            while left <= right and (cmp(arr[left], pivot) == -1 or cmp(pivot, arr[left]) == 1):
                left += 1 
            while left <= right and (cmp(arr[right], pivot) == 1 or cmp(pivot, arr[right]) == -1):
                right -= 1 
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1 
                right -= 1
        arr[start], arr[right] = arr[right], arr[start]
        return right
        
        