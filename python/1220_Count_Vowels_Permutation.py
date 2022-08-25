class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0] * 5 for _ in range(n)]
        BASE = 1000000007
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            dp[i][0] = (dp[i - 1][1] + dp[i - 1][4] + dp[i - 1][2]) % BASE
            dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % BASE
            dp[i][2] = (dp[i - 1][1] + dp[i - 1][3]) % BASE
            dp[i][3] = (dp[i - 1][2]) % BASE
            dp[i][4] = (dp[i - 1][3] + dp[i - 1][2]) % BASE
        return sum(dp[n - 1]) % BASE
        