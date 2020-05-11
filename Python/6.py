class Solution:
    def convert(self, s, numRows):
        if numRows <=1 or numRows >= len(s):
            return s
        arr = [''] * numRows
        line = 0
        step = -1
        for c in s:
            arr[line] += c
            if line % (numRows-1) == 0:
                step = -step
            line += step
        return ''.join(arr)  