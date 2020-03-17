class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        # num = ord('a')
        # letters = []
        # for i in range(26):
        #     letters.append(chr(num + i))
        half = len(palindrome) // 2 

        for i in range(half):
            if palindrome[i] != 'a' :
                res = palindrome[:i] + 'a' + palindrome[i + 1:]
                return res
        
        return palindrome[:-1] + 'b' if len(palindrome) > 1 else ""