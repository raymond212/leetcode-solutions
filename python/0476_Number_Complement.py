class Solution:
    def findComplement(self, num: int) -> int:
        if num == 0:
            return 1
        mask = 0
        temp = num
        while temp > 0:
            mask = (mask << 1) | 1
            temp >>= 1
        return num ^ mask