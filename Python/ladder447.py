class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1 
        left = (index - 1) // 2 
        right = index + 1
        while left + 1 < right:
            mid = (left + right) // 2 
            if reader.get(mid) < target:
                left = mid 
            else:
                right = mid
                
        if reader.get(left) == target:
            return left 
        if reader.get(right) == target:
            return right
        return -1