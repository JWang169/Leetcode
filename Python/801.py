class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        n = len(A)
        # swap[i]: minimum swap times to make A[:i], B[:i] increasing, with swap on A[i] and B[i]
        # notSwap[i]: minimum swap times to make A[:i], B[:i] increasing, without swap on A[i] and B[i]

        swap = [n] * n
        notSwap = [n] * n 
        swap[0] = 1
        notSwap[0] = 0
        
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]:
                # two options: 1. dont swap at i - 1 and dont swap at i;  2. swap at i - 1 and swap at i
                # the min is trivial, because notSwap is garanteed to be mininum. 
                notSwap[i] = notSwap[i - 1]
                swap[i] = swap[i - 1] + 1
            
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                # two options: 1. dont swap at i - 1 and 
                notSwap[i] = min(swap[i - 1], notSwap[i])
                swap[i] = min(notSwap[i - 1] + 1, swap[i])
        return min(notSwap[-1], swap[-1])