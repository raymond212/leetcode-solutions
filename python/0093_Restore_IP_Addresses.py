class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        addresses = []
        self.dfs(s, 0, 4, [], addresses)
        return addresses
    
    def dfs(self, s, index, remain, address, addresses):
        if remain == 0: 
            if index == len(s):
                addresses.append(self.convert(address))
            return
        
        if index >= len(s):
            return

        if s[index] == "0":
            address.append(0)
            self.dfs(s, index + 1, remain - 1, address, addresses)
            address.pop()
            return

        for length in range(1, 4):
            if index + length > len(s):
                continue
            integer = int(s[index: index + length])
            if 0 <= integer <= 255:
                address.append(integer)
                self.dfs(s, index + length, remain - 1, address, addresses)
                address.pop()
    
    def convert(self, address):
        s = ""
        for i in range(0, len(address) - 1):
            s += str(address[i]) + "."
        s += str(address[-1])
        return s