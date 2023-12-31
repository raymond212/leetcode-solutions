class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        ans = -1

        for i, c in enumerate(s):
            if c in first:
                ans = max(ans, i - first[c] - 1)
            else:
                first[c] = i
        
        return ans