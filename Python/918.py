class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        total = 0
        prevMax = 0
        prevMin = 0
        minimum = sys.maxsize
        f = [0] * len(A)
        for i in range(len(A)):
            total += A[i]
            f[i] = max(prevMax + A[i], A[i])
            prevMax = f[i]
            if prevMin >= 0:
                prevMin = A[i]
            else:
                prevMin += A[i]
            minimum = min(minimum, prevMin)

        maximum = max(f)
        if maximum > 0:
            return max(maximum, total - minimum)
        else:
            return maximum