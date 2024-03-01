class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        cnt = s.count('1')
        return '1' * (cnt - 1) + '0' * (len(s) - cnt) + '1'