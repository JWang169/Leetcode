class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = {}
        for word in strs:
            key = ''.join(sorted(word))
            pairs[key] = pairs.get(key, list())
            pairs[key].append(word)
       
        result = []
        for key in pairs.keys():
            result.append(pairs[key])
        
        return result     
        
        