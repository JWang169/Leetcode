class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        # return collections.Counter(target) == collections.Counter(arr)
        dicTarget = dict()
        for char in target:
            dicTarget[char] = dicTarget.get(char, 0) + 1
        dicArr = dict()
        for char in arr:
            dicArr[char] = dicArr.get(char, 0) + 1
        
        if len(dicTarget) != len(dicArr):
            return False
        
        for key, val in dicTarget.items():
            if key not in dicArr or val != dicArr[key]:
                return False
        return True