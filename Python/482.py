class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        chars = "".join(S.split("-"))
        n = len(chars)
        result = ""
        if n % K:
            result += chars[: n % K]
        start = n % K

        while start < n:
            if start > 0:
                result += "-"
            result += chars[start: start + K]
            start += K

        return result.upper()
        
        
        