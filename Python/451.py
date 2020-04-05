class Solution:
    def frequencySort(self, s: str) -> str:
        count = collections.Counter(s)
        mappings = collections.defaultdict(list)
        for key, value in count.items():
            mappings[value].append(key)
        
        result = ""
        ks = list(mappings.keys())
        ks.sort(reverse=True)
        for num in ks:
            for ch in mappings[num]:
                result += ch * num
        return result 
        
        
        