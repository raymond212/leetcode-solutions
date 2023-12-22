class Solution:
    def maxScore(self, s: str) -> int:
        zeros = ones = 0
        num_ones = s.count('1')
        ans = 0

        for i in range(len(s)):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            if i < len(s) - 1:
                ans = max(ans, num_ones + zeros - ones)
        
        return ans