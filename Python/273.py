class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """        
        matches = {1: 'One', 2: 'Two', 3:'Three', 4: 'Four' , 5:'Five', 6: 'Six', 7: 'Seven', 8:'Eight', 9:'Nine', 10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40:'Forty', 50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', 90: 'Ninety'}
        
        def helper(n):
            if n // 1000000000:
                return helper(n // 1000000000) + 'Billion ' + helper(n % 1000000000)
            
            elif n // 1000000:
                return helper(n // 1000000) + 'Million ' + helper(n % 1000000)
            
            elif n // 1000:
                return helper(n // 1000) + 'Thousand ' + helper(n % 1000)
            
            elif n // 100:
                return  matches[n // 100] + ' Hundred ' + helper(n % 100)
            
            elif n >= 20: 
                return  matches[n // 10 * 10] + ' ' + helper(n % 10) 
            
            elif n > 0:
                return matches[n] + ' '
            
            return ''
        if num == 0:
            return 'Zero'
        
        res = helper(num)
        return res.strip()