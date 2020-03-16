class Solution:
    def validIPAddress(self, IP: str) -> str:
        # if not IP:
        #     return "Neither"
        if len(IP.split('.')) == 4:
            ips = IP.split('.')
            return self.validIPv4(ips)
        elif len(IP.split(':')) == 8:
            ips = IP.split(':')
            return self.validIPv6(ips)
        return "Neither"
    
    
    def validIPv4(self, ips):
        for number in ips:
            # no leading zero
            if len(number) > 1 and number[0] == '0':
                return "Neither"
            
            # 0 to 255
            if number.isdigit() and 0 <= int(number) <= 255:
                continue
            else:
                return "Neither"
        return "IPv4"
    
    
    def validIPv6(self, ips):
        hexSet = set(['a', 'b', 'c', 'd', 'e', 'f'])
        for numbers in ips:
            # empty group or too long
            if len(numbers) == 0 or len(numbers) > 4:
                return "Neither"
            
            for idx, num in enumerate(numbers):
                if not num.isdigit() and num.lower() not in hexSet:
                    print("char not valid")
                    return "Neither"  

                
        return "IPv6"
    
    