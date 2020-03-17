class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers2(self, A):
        # quick sort 
        self.mergeSort(A)
    
    
    
    def quickSort(self, A, start, end):
        if start >= end:
            return 
        left, right = start, end 
        mid = (left + right) // 2 
        pivot = A[mid]
        while left <= right:
            while left <= right and A[left] < pivot:
                left += 1 
            while left <= right and A[right] > pivot:
                right -= 1 
            if left <= right:
                A[left], A[right] = A[right], A[left]
                left += 1 
                right -= 1 
        
        self.quickSort(A, start, right)
        self.quickSort(A, left, end)
        
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return 
        mid = len(nums) // 2 
        L = list(nums[:mid])
        R = list(nums[mid:])
        
        # sort the first and second half
        self.mergeSort(L)
        self.mergeSort(R)
        
        i = j = k = 0
        # copy data to temp arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                nums[k] = L[i]
                i += 1 
            else:
                nums[k] = R[j]
                j += 1 
            k += 1 
        
        while i < len(L):
            nums[k] = L[i]
            i += 1 
            k += 1 
        while j < len(R):
            nums[k] = R[j]
            j += 1 
            k += 1 
            
       
            
        
        
        