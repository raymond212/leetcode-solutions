class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target > n * k or target < n:
            return 0

        # dp[i][j]: number of ways to make j with i die
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            ways = 0
            for j in range(1, min(target, i * k) + 1):
                ways += dp[i - 1][j - 1]
                if j - k - 1 > 0:
                    ways -= dp[i - 1][j - k - 1]
                dp[i][j] = ways
        
        return dp[n][target] % int(1e9 + 7)