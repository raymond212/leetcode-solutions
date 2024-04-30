class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cur = 0
        dp = [0] * 1024
        dp[0] = 1
        res = 0

        for c in word:
            cur ^= (1 << (ord(c) - ord('a')))
            res += dp[cur]
            for i in range(10):
                res += dp[cur ^ (1 << i)]
            dp[cur] += 1

        return res 