class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first = {}
        last = {}
        n = len(s)

        for i in range(n):
            if s[i] not in first:
                first[s[i]] = i

        for i in range(n - 1, -1, -1):
            if s[i] not in last:
                last[s[i]] = i

        ans = -1
        for c in first:
            if first[c] == last[c]:
                continue
            ans = max(ans, last[c] - first[c] - 1)
        
        return ans
