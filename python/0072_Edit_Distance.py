class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 is None or word2 is None:
            return -1

        n, m = len(word1), len(word2)

        # state
        dp = [[0] * (m + 1) for _ in range(2)]

        # initialization
        for j in range(m + 1):
            dp[0][j] = j

        # function
        for i in range(1, n + 1):
            dp[i % 2][0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1, dp[(i - 1) % 2][j - 1])
                else:
                    dp[i % 2][j] = min(dp[(i - 1) % 2][j] + 1, dp[i % 2][j - 1] + 1, dp[(i - 1) % 2][j - 1] + 1)

        return dp[n % 2][m]