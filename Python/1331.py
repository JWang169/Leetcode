class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = dict()
        nums = sorted(arr)
        rank = 1
        prev = None 
        for num in nums:
            if num == prev:
                continue
            ranks[num] = rank
            rank += 1 
            prev = num
        
        result = []
        for num in arr:
            result.append(ranks[num])
            
        return result
        
        