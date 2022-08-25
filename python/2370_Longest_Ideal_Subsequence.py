class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        if not s:
            return 0
        n = len(s)
        dp = [1] * n # dp[i] represents the length of the longest ideal string ending on s[i]
        max_for_letter = [0] * 26
        max_for_letter[ord(s[0]) - ord('a')] = 1
        
        for i in range(1, n):
            pos = ord(s[i]) - ord('a')
            for j in range(26):
                if abs(j - pos) <= k:
                    dp[i] = max(dp[i], max_for_letter[j] + 1)
            max_for_letter[pos] = max(max_for_letter[pos], dp[i])
        return max(dp)