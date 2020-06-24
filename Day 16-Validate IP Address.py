class Solution:
    def validIPAddress(self, IP: str) -> str:
        ipv4=re.search('^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$',IP)
        ipv6 = re.search('^([\da-f]{1,4}:){7}[\da-f]{1,4}$',IP,re.I)
        if ipv4:
            return 'IPv4'
        elif ipv6:
            return 'IPv6'
        else:
            return 'Neither'
        
    
