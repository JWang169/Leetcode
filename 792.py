class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        seqs = collections.defaultdict(list)
        for i, ch in enumerate(S):
            seqs[ch].append(i)
        count = 0


        for word in words:
            pointer = -1
            found = True
            for ch in word:
                if ch not in seqs:
                    found = False
                    break
                idx = bisect.bisect_left(seqs[ch], pointer)
                # print('idx: ', idx, 'ch: ', ch, 'pointer: ',pointer)
                if idx < len(seqs[ch]) and seqs[ch][idx] >= pointer:
                    pointer = seqs[ch][idx] + 1
                else:
                    found = False
                    break   
                
            if found:
                count += 1 
        return count 
            
        
        
        
        
        