class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        res = 1
        prevInd = 0
        prevChar = s[0]
        for i in range(1, len(s)):
            if ord(s[i]) - ord(prevChar) == 1:
                prevChar = s[i]
                continue
            res = max(res, i - prevInd)
            prevInd = i
            prevChar = s[i]
        res = max(res, len(s) - prevInd)
        return res