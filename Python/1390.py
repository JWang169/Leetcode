class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            count = 2
            divisor = 2
            divs = [1, num]
            while len(divs) <= 4 and divisor * divisor <= num:
                if num % divisor == 0:
                    divs.append(divisor)
                    if num // divisor != divisor:
                        divs.append(num // divisor)
                divisor += 1
            if len(divs) == 4:
                result += sum(divs)
        return result
        
        
        
        